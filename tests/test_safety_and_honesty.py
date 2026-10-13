import json

from afya_ya_akili_mcp import server

_fn = lambda name: (getattr(server, name).fn if hasattr(getattr(server, name), "fn") else getattr(server, name))


def test_the_verified_crisis_facts_are_unchanged():
    """Life-safety content: the directory is verified data, and a description rewrite must not move it."""
    d = _fn("crisis_line_directory")()
    assert "999" in d["emergency"] and "112" in d["emergency"]
    bef = next(x for x in d["crisis_lines"] if x["name"] == "Befrienders Kenya")
    assert bef["number"] == "+254 722 178 177" and "NOT 24/7" in bef["hours"]
    other = next(x for x in d["crisis_lines"] if x["number"] == "0800 723 253")
    assert "NOT Befrienders" in other["note"]


def test_the_rights_summary_no_longer_asserts_things_that_could_not_be_verified():
    text = json.dumps(_fn("mental_health_rights")(None))
    assert "Mental Health Tribunal" not in text and "within 7 days" not in text and "Disability Discrimination Act" not in text
    assert "UNVERIFIED" in text and "Cap 248" in text


def test_an_unknown_county_or_provider_type_is_flagged_not_silently_widened():
    r = _fn("mental_health_provider_finder")("Atlantis", None)
    assert r["resources"] == [] and "crisis_line_directory" in r["note"]
    assert _fn("mental_health_provider_finder")(None, "zzz")["provider_type_matched"] is False
    assert _fn("mental_health_provider_finder")(None, "private_clinic")["provider_type_matched"] is True
    assert _fn("mental_health_provider_finder")(None, "psychiatrist")["provider_type_matched"] is False  # a profession, not a facility type
