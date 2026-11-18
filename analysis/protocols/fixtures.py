"""Fixtures definitions, updated for plan v2.9 (not research data).

Không đọc dữ liệu nghiên cứu. Mọi con số là ví dụ nhân tạo dùng để chốt định nghĩa.
Chạy: python -I fixtures.py  (in JSON ra stdout)
"""
import json
from fractions import Fraction as F


# --- F1 (N02): mean-of-ratios khác ratio-of-totals -------------------------
def f1_aggregation():
    # Hai cặp câu. T_EN = số token bản tiếng Anh, T_L = số token bản ngôn ngữ L.
    # T_EN phai khac nhau giua cac cap, neu khong hai cach gop trung nhau
    pairs = [(10, 5), (20, 40)]  # (T_EN, T_L)
    ratio_of_totals = F(sum(l for _, l in pairs), sum(e for e, _ in pairs))
    mean_of_ratios = sum(F(l, e) for e, l in pairs) / len(pairs)
    mean_L_over_mean_EN = F(sum(l for _, l in pairs), len(pairs)) / F(
        sum(e for e, _ in pairs), len(pairs)
    )
    return {
        "pairs_T_EN_T_L": pairs,
        "ratio_of_totals": float(ratio_of_totals),
        "mean_of_ratios": float(mean_of_ratios),
        "mean_T_L_over_mean_T_EN": float(mean_L_over_mean_EN),
        "ratio_of_totals_equals_mean_over_mean": ratio_of_totals == mean_L_over_mean_EN,
        "mean_of_ratios_differs": mean_of_ratios != ratio_of_totals,
        "ket_luan": (
            "mean(T_L)/mean(T_EN) BANG ratio-of-totals khi cung so cap; "
            "mean(T_L/T_EN) KHAC. Phai khoa primary aggregation truoc test."
        ),
    }


# --- F2 (N02): identity PFR/Tax = sum(W_L)/sum(W_EN), chi khi cung tap cap --
def f2_identity():
    # (T_EN, W_EN, T_L, W_L) cho tung cap
    rows = [(10, 4, 20, 3), (14, 6, 25, 5)]
    sT_EN = sum(r[0] for r in rows); sW_EN = sum(r[1] for r in rows)
    sT_L = sum(r[2] for r in rows);  sW_L = sum(r[3] for r in rows)
    pfr_total = F(sT_L, sT_EN)
    tax_total = F(sT_L, sW_L) / F(sT_EN, sW_EN)
    lhs = pfr_total / tax_total
    rhs = F(sW_L, sW_EN)
    # Doi corpus: tinh tax tren mot tap cap khac -> identity gay
    rows_other = [(12, 5, 30, 4)]
    tax_other = F(sum(r[2] for r in rows_other), sum(r[3] for r in rows_other)) / F(
        sum(r[0] for r in rows_other), sum(r[1] for r in rows_other)
    )
    return {
        "same_corpus": {
            "PFR_total": float(pfr_total),
            "Tax_total": float(tax_total),
            "PFR_over_Tax": float(lhs),
            "sumW_L_over_sumW_EN": float(rhs),
            "identity_holds": lhs == rhs,
        },
        "cross_corpus": {
            "Tax_tu_corpus_khac": float(tax_other),
            "PFR_over_Tax_cross": float(pfr_total / tax_other),
            "sumW_L_over_sumW_EN_cua_corpus_goc": float(rhs),
            "identity_holds": (pfr_total / tax_other) == rhs,
        },
        "ket_luan": (
            "Identity chi dung cho ratio-of-totals tren CUNG tap cap va cung "
            "counting policy. Khac corpus thi ti so khong con la sumW_L/sumW_EN, "
            "nen khong suy ra duoc so tu hay morphology."
        ),
    }


# --- F3 (N05/RQ3): rescale duong hang so giu nguyen AUC trong ngon ngu -----
def _auc(pos, neg):
    n = F(0); d = 0
    for p in pos:
        for q in neg:
            d += 1
            n += F(1) if p > q else (F(1, 2) if p == q else F(0))
    return n / d


def f3_rescale_invariance():
    pos = [F(3), F(1), F(2)]
    neg = [F(0), F(-1), F(5)]
    base = _auc(pos, neg)
    c = F(7, 3)  # hang so duong, ap cho MOI tai lieu trong ngon ngu
    scaled = _auc([c * x for x in pos], [c * x for x in neg])
    # Bien doi phu thuoc tai lieu: chia theo T_d/G_d rieng tung tai lieu
    tg_pos = [F(6), F(1, 2), F(1)]
    tg_neg = [F(1), F(1), F(10)]
    doc_dep = _auc([x / t for x, t in zip(pos, tg_pos)], [x / t for x, t in zip(neg, tg_neg)])
    return {
        "auc_goc": float(base),
        "auc_sau_rescale_hang_so_duong": float(scaled),
        "bat_bien": base == scaled,
        "auc_sau_bien_doi_phu_thuoc_tai_lieu": float(doc_dep),
        "doi_khi_phu_thuoc_tai_lieu": base != doc_dep,
        "ket_luan": (
            "RQ3 nguyen van khong the duoc tra loi bang mot hang so duong theo "
            "ngon ngu: local AUC bat bien. Can phep bien doi doi thu hang cap tai lieu."
        ),
    }


# --- F4 (N04): fixture bat translated-duplicate vi pham family split -------
def f4_family_split():
    # family_id dung chung cho moi ban dich cua cung noi dung
    records = [
        {"id": "en-001", "family": "F1", "lang": "en", "split": "exposure"},
        {"id": "vi-001", "family": "F1", "lang": "vi", "split": "holdout"},   # VI PHAM
        {"id": "en-002", "family": "F2", "lang": "en", "split": "exposure"},
        {"id": "ta-002", "family": "F2", "lang": "ta", "split": "exposure"},  # hop le
        {"id": "en-003", "family": "F3", "lang": "en", "split": "holdout"},
        {"id": "te-003", "family": "F3", "lang": "te", "split": "holdout"},   # hop le
    ]
    for r in records:
        r['adapter'] = 'A1'
    # Different targets can have different exposure for the same family.
    records.append({'id': 'vi-002', 'family': 'F2', 'lang': 'vi',
                    'split': 'holdout', 'adapter': 'A2'})
    by_family = {}
    for r in records:
        by_family.setdefault((r['adapter'], r['family']), set()).add(r['split'])
    violations = sorted(f for f, s in by_family.items() if len(s) > 1)
    assert violations == [('A1', 'F1')]
    return {
        "so_ban_ghi": len(records),
        "family_vi_pham": violations,
        "phat_hien_duoc": violations == [('A1', 'F1')],
        "ket_luan": (
            "Family policy ap theo target adapter/checkpoint. Cross-language "
            "exposure/holdout trong A1 vi pham primary policy; khac adapter "
            "khong tu dong vi pham. Detector test van duoc chua target members."
        ),
    }


# --- F5 (N01): workload cua hai nhanh adapter -----------------------------
def f5_workload(models=3, langs=8, seeds=3, exposure_tokens_per_lang=1_000_000,
                score_tokens_per_lang=200_000):
    per_lang_runs = models * langs * seeds
    multi_runs = models * seeds
    modes = {}
    # Che do A: giu exposure MOI NGON NGU co dinh
    modes["giu_exposure_moi_ngon_ngu"] = {
        "per_language": {
            "adapters": per_lang_runs,
            "train_tokens": per_lang_runs * exposure_tokens_per_lang,
            "model_loads_if_cold_start_each_adapter": per_lang_runs,
        },
        "multilingual": {
            "adapters": multi_runs,
            "train_tokens": multi_runs * langs * exposure_tokens_per_lang,
            "model_loads_if_cold_start_each_adapter": multi_runs,
        },
    }
    a = modes["giu_exposure_moi_ngon_ngu"]
    a["train_tokens_bang_nhau"] = (
        a["per_language"]["train_tokens"] == a["multilingual"]["train_tokens"]
    )
    a['cold_start_load_ratio'] = per_lang_runs / multi_runs
    a['reuse_base_loads_example_both_branches'] = models
    # Che do B: giu NGAN SACH MOI RUN co dinh (run multilingual bang run don ngu)
    modes["giu_ngan_sach_moi_run"] = {
        "per_language": {
            "adapters": per_lang_runs,
            "train_tokens": per_lang_runs * exposure_tokens_per_lang,
            "exposure_moi_ngon_ngu_moi_seed": exposure_tokens_per_lang,
        },
        "multilingual": {
            "adapters": multi_runs,
            "train_tokens": multi_runs * exposure_tokens_per_lang,
            "exposure_moi_ngon_ngu_moi_seed": exposure_tokens_per_lang / langs,
        },
        "ti_so_train_tokens": langs,
        "canh_bao": (
            "Giu ngan sach moi run thi multilingual re hon 8 lan ve train tokens, "
            "NHUNG moi ngon ngu chi con 1/8 exposure, tac dong AUC chua biet. "
            "Day la THI NGHIEM KHAC, khong phai cung mot thi nghiem gop lai."
        ),
    }
    # Scoring 0x khong doi theo nhanh
    scoring = {
        "scored_tokens": models * langs * score_tokens_per_lang,
        "ghi_chu": "Gop adapter khong lam giam luong text phai cham o moc 0x.",
    }
    return {
        "gia_dinh": {
            "models": models, "langs": langs, "seeds": seeds,
            "exposure_tokens_per_lang": exposure_tokens_per_lang,
            "score_tokens_per_lang": score_tokens_per_lang,
        },
        "modes": modes,
        "scoring_0x": scoring,
        "ket_luan": (
            "72 va 9 la so ADAPTER. Duoi che do giu exposure moi ngon ngu, train "
            "tokens BANG NHAU; model loads phu thuoc cold start hay reuse, "
            "throughput/retry can profiling. Khong suy giam 8x thoi gian."
        ),
    }


if __name__ == "__main__":
    out = {
        "muc_dich": "Fixture definitions plan v2.9; synthetic only, not approval or pilot data",
        "F1_aggregation_N02": f1_aggregation(),
        "F2_identity_N02": f2_identity(),
        "F3_rescale_invariance_N05_RQ3": f3_rescale_invariance(),
        "F4_family_split_N04": f4_family_split(),
        "F5_workload_N01": f5_workload(),
    }
    assert out['F1_aggregation_N02']['ratio_of_totals_equals_mean_over_mean']
    assert out['F1_aggregation_N02']['mean_of_ratios_differs']
    assert out['F2_identity_N02']['same_corpus']['identity_holds']
    assert not out['F2_identity_N02']['cross_corpus']['identity_holds']
    assert out['F3_rescale_invariance_N05_RQ3']['bat_bien']
    assert out['F3_rescale_invariance_N05_RQ3']['doi_khi_phu_thuoc_tai_lieu']
    assert out['F4_family_split_N04']['phat_hien_duoc']
    assert out['F5_workload_N01']['modes']['giu_exposure_moi_ngon_ngu']['train_tokens_bang_nhau']
    print(json.dumps(out, ensure_ascii=False, indent=2))
