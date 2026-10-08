"""Life-safety content. These tests encode the specific mistakes found on 2026-10-07: Befrienders Kenya was given another organisation's number and a 24/7 claim,
its real number was attached to two other organisations, and a non-Kenyan helpline was listed as Kenyan."""
import pathlib
from collections import defaultdict

from afya_ya_akili_mcp import server

ROOT = pathlib.Path(__file__).resolve().parents[1]
call = lambda name, *a, **k: (getattr(server, name).fn if hasattr(getattr(server, name), "fn") else getattr(server, name))(*a, **k)


def lines():
    return {x["name"]: x for x in call("crisis_line_directory")["crisis_lines"]}


def test_befrienders_kenya_has_its_own_number_and_honest_hours():
    b = lines()["Befrienders Kenya"]
    assert b["number"] == "+254 722 178 177" and "NOT 24/7" in b["hours"] and "Mon-Fri" in b["hours"]


def test_no_number_is_attached_to_two_different_organisations():
    owners = defaultdict(set)
    for x in call("crisis_line_directory")["crisis_lines"]:
        owners[x["number"].replace(" ", "")].add(x["name"])
    assert all(len(v) == 1 for v in owners.values()), dict(owners)


def test_the_emergency_medicine_foundation_number_is_not_presented_as_befrienders():
    ls = lines()
    assert "723 253" not in ls["Befrienders Kenya"]["number"] and ls["Emergency Medicine Kenya Foundation"]["number"] == "0800 723 253"
    assert "NOT Befrienders" in ls["Emergency Medicine Kenya Foundation"]["note"]


def test_every_entry_says_how_well_it_is_confirmed_and_single_listings_are_flagged():
    for x in call("crisis_line_directory")["crisis_lines"]:
        assert isinstance(x["listings_confirming"], int) and x["listings_confirming"] >= 1 and x["hours"] and x["number"]
        if x["listings_confirming"] == 1:
            assert "confirm" in x["note"].lower()


def test_the_source_does_not_claim_demo_data_is_verified():
    assert "verified crisis lines" not in call("crisis_line_directory")["source"] and "2026-10-07" in call("crisis_line_directory")["source"]


def test_the_server_instructions_give_the_right_befrienders_number():
    ins = server.mcp.instructions
    assert "+254 722 178 177" in ins and "0800 723 253" not in ins


def test_no_non_kenyan_helpline_is_listed_and_the_old_wrong_pairing_is_gone_everywhere():
    assert "iCall" not in str(call("self_help_resources")) and "icallhelpline" not in str(call("crisis_line_directory"))
    for f in (ROOT / "src" / "afya_ya_akili_mcp" / "server.py", ROOT / "README.md"):
        assert "Befrienders Kenya 0800 723 253" not in f.read_text(encoding="utf-8") and '"Befrienders Kenya", "number": "0800' not in f.read_text(encoding="utf-8")
