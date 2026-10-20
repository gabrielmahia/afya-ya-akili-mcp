"""AfyaYaAkiliMCP — Kenya Mental Health Resources (5 tools). All data DEMO."""
from __future__ import annotations

from typing import Annotated, Optional

from fastmcp import FastMCP
from pydantic import Field

# Annotations tell clients which tools are safe to auto-approve (read-only, no side effects).
READ_ONLY = {"readOnlyHint": True, "idempotentHint": True, "openWorldHint": False}

mcp = FastMCP(name="afya-ya-akili-mcp", instructions="Kenya mental health resources, hand-compiled and partly unverified (read each answer's source). Not a substitute for emergency or clinical care. If life is at risk call 999 or 112. Befrienders Kenya: +254 722 178 177 (call, SMS or WhatsApp; Mon-Fri 9am-5pm). Kenya Red Cross: 1199.")

@mcp.tool(name="mental_health_provider_finder", description="Find sample mental health providers and services in Kenya by county and facility type, with a guide to what each kind of professional does (psychiatrist, psychologist, counsellor, psychotherapist). Use when someone asks where to get professional help. county filters by matching text; an unmatched county returns an empty list with a note. provider_type filters by FACILITY type (public_hospital, private_clinic, private_hospital, crisis_support or training_clinic); the professional titles in the guide are explanations, not filter values. If provider_type matches nothing, ALL providers are returned and provider_type_matched is false. Returns the source label, the resources with type, county, note and contact, the guide, KPA and KCA pointers and an SHA note. A short hand-compiled sample: phone numbers other than Befrienders Kenya's are NOT verified, so confirm before use. For someone in crisis use crisis_line_directory first. Read-only; no side effects.", annotations=READ_ONLY)
def mental_health_provider_finder(county: Annotated[str | None, Field(description="Optional county such as Nairobi; matched by text.")] = None, provider_type: Annotated[str | None, Field(description="Optional facility type: public_hospital, private_clinic, private_hospital, crisis_support or training_clinic. Professional titles such as psychiatrist do not match.")] = None) -> dict:
    TYPES = {"psychiatrist": "Medical doctor specialising in mental health. Prescribes medication.",
             "psychologist":  "Assesses and provides therapy. Cannot prescribe medication in Kenya.",
             "counselor":     "KCPA/KCA registered counsellor. Talk therapy, shorter training.",
             "psychotherapist":"Longer-term talk therapy. Various modalities (CBT, psychodynamic)."}
    RESOURCES = [
        {"name": "Mathare Hospital", "type": "public_hospital", "county": "Nairobi",
         "note": "Kenya's main public psychiatric hospital. SHA accreditation status UNVERIFIED.", "contact": "020-2001000"},
        {"name": "Chiromo Lane Medical Centre", "type": "private_clinic", "county": "Nairobi",
         "note": "Comprehensive psychiatric care. Private.", "contact": "020-2014469"},
        {"name": "Befrienders Kenya", "type": "crisis_support", "county": "Nairobi",
         "note": "Emotional support for distress or suicidal thoughts. Free and confidential. Call, SMS or WhatsApp; Mon-Fri 9am-5pm per its own listing, not 24/7.", "contact": "+254 722 178 177"},
        {"name": "Aga Khan University Hospital — Psychiatry", "type": "private_hospital", "county": "Nairobi",
         "note": "Outpatient and inpatient psychiatry. SHA cover for some cases (UNVERIFIED).", "contact": "020-3662000"},
        {"name": "USIU-Africa Counselling Centre", "type": "training_clinic", "county": "Nairobi",
         "note": "Affordable counselling by supervised trainees.", "contact": "020-3606000"},
    ]
    if county:
        RESOURCES = [r for r in RESOURCES if county.lower() in r["county"].lower()]
    provider_matched = None
    if provider_type:
        by_type = [r for r in RESOURCES if provider_type.lower() in r["type"]]
        provider_matched = bool(by_type)
        RESOURCES = by_type or RESOURCES
    note = "No sample providers for this county. Use crisis_line_directory, and the KPA and KCA links below." if not RESOURCES else None
    return {"source": "DEMO — hand-compiled. Phone numbers other than Befrienders Kenya's (verified 2026-10-07) are NOT verified: confirm before use", "county": county,
            "resources": RESOURCES, "provider_type_matched": provider_matched, "note": note, "provider_type_guide": TYPES, "kpa": "Kenya Psychiatric Association: psychiatry.or.ke",
            "kca": "Kenya Counsellors Association: kcaglobal.com",
            "nhif": "Inpatient psychiatric care may be covered through SHA (which replaced NHIF in Oct 2024); scope UNVERIFIED, check sha.go.ke"}

@mcp.tool(name="crisis_line_directory", description="Kenya emergency and mental health crisis lines compiled from public listings on 2026-10-07. Use when someone is in distress, mentions self-harm or suicidal thoughts, or asks for a helpline. If life is at risk, tell them first to call 999 or 112 or go to the nearest hospital emergency department, then offer this list. Takes no arguments. Returns the emergency numbers, then each line's number, hours, channels and cost, how many independent listings confirm it (a low count means unconfirmed), and the numbers removed because they could not be verified. Befrienders Kenya is NOT 24/7 (weekday daytime hours per its own listing). Numbers and hours change: confirm before relying. Not a substitute for emergency services or professional care. Read-only; no side effects.", annotations=READ_ONLY)
def crisis_line_directory() -> dict:
    return {
        "source": "Compiled from public listings on 2026-10-07: Befrienders Kenya's own listing via Lifeline International and Find A Helpline; Kenya Red Cross and emergency numbers via HapaKenya and Standard Media; NACADA and the child helpline via Find A Helpline. Numbers change: confirm before relying.",
        "emergency": "If life is at risk call 999 or 112 (911 also connects from Safaricom), or go to the nearest hospital emergency department.",
        "crisis_lines": [
            {"name": "Befrienders Kenya", "number": "+254 722 178 177", "channels": "call, SMS, WhatsApp", "cost": "free",
             "hours": "Mon-Fri 9am-5pm per its own listing (one other listing says 7am-7pm); NOT 24/7", "listings_confirming": 4,
             "note": "Free, confidential emotional support for distress, self-harm and suicidal thoughts. Outside these hours use 999/112, 1199 or a hospital emergency department."},
            {"name": "Kenya Red Cross", "number": "1199", "channels": "call", "cost": "toll-free", "hours": "24/7 per HapaKenya (2026-03)", "listings_confirming": 3,
             "note": "Toll-free humanitarian line; listed as a free national mental health helpline."},
            {"name": "Police and general emergency", "number": "999 or 112 (911 from Safaricom)", "channels": "call", "cost": "toll-free", "hours": "24/7", "listings_confirming": 2,
             "note": "Fire, ambulance and police."},
            {"name": "NACADA", "number": "1192", "channels": "call", "cost": "toll-free", "hours": "24-hour per OpenCounseling", "listings_confirming": 3,
             "note": "Alcohol and drug abuse."},
            {"name": "National Child Helpline", "number": "116", "channels": "call", "cost": "free", "hours": "24/7 per Find A Helpline", "listings_confirming": 2,
             "note": "Children and young people."},
            {"name": "Emergency Medicine Kenya Foundation", "number": "0800 723 253", "channels": "call", "cost": "toll-free", "hours": "not stated", "listings_confirming": 2,
             "note": "Listed under crisis lines by two secondary listings only: confirm. This is NOT Befrienders Kenya's number (earlier versions of this server attached it to Befrienders)."},
            {"name": "Gender Violence Recovery Centre", "number": "0800 720 565", "channels": "call", "cost": "toll-free", "hours": "not stated", "listings_confirming": 1,
             "note": "Gender-based violence. Single listing (TherapyRoute): confirm."},
        ],
        "not_included": "Earlier versions listed other numbers, an online counselling service that is not Kenyan, and a '24-hour psychiatric emergency' line that reused Befrienders' number; none could be verified, so they were removed.",
        "note": "If you or someone you know is in immediate danger, go to the nearest hospital emergency department.",
    }


@mcp.tool(name="mental_health_rights", description="Summarise patient rights under Kenya's Mental Health Act (Cap 248, amended in 2022): consent, confidentiality, voluntary treatment, dignity, challenging involuntary admission, community care, discrimination and insurance. Use when someone asks what rights they or a relative have in treatment. Keywords in topic select entries; if none match, ALL rights are returned. Returns the source label, topic, the rights, a disclaimer and the regulators. A summary labelled DEMO and partly unverified: the appeal, discrimination and insurance entries say what is not confirmed. Not legal advice: read the Act on kenyalaw.org or ask a lawyer. Read-only; no side effects.", annotations=READ_ONLY)
def mental_health_rights(topic: Annotated[str | None, Field(description="Optional topic such as consent, confidentiality, appeal or insurance.")] = None) -> dict:
    RIGHTS = {
        "consent":        "No person may be admitted or treated without free and informed consent, except under emergency or court order.",
        "confidentiality":"Mental health records are confidential. Cannot be disclosed without consent (subject to safety exceptions).",
        "voluntary":      "Right to seek voluntary treatment without involuntary admission.",
        "dignity":        "Right to be treated with dignity. No cruel treatment in mental health facilities.",
        "appeal":         "Involuntary admission can be challenged before the Mental Health Review Board (as reported by the press; initial detention is reported as up to 48 hours before longer stays need the Board). Time limits and procedure are UNVERIFIED against the Act: read the Mental Health Act (Cap 248) on kenyalaw.org or ask a lawyer.",
        "community":      "Right to community-based mental health care, not just institutional.",
        "discrimination": "The Persons with Disabilities Act, 2003 and Article 27 of the Constitution prohibit discrimination on grounds of disability. Whether and how they cover a particular mental health condition is UNVERIFIED here.",
        "insurance":      "The Mental Health Act has a section on insurance for the treatment of mental disorder (section 46 in the 1989 text). What it now requires is UNVERIFIED here: ask the insurer in writing and read the section on kenyalaw.org.",
    }
    if topic:
        t = topic.lower()
        matched = {k: v for k, v in RIGHTS.items() if k in t or any(w in t for w in k.split("_"))}
        return {"source": "DEMO, partly unverified — Mental Health Act (Cap 248) as amended by the Mental Health (Amendment) Act, 2022", "topic": topic,
                "rights": matched or RIGHTS, "disclaimer": "Not legal advice."}
    return {"source": "DEMO, partly unverified — Mental Health Act (Cap 248) as amended by the Mental Health (Amendment) Act, 2022 (Act No. 27 of 2022, in force 11 July 2022); kenyalaw.org", "rights": RIGHTS,
            "regulator": "Mental Health Review Board and the Kenya Board of Mental Health (names as reported; confirm in the Act). Kenya Medical Practitioners and Dentists Council (KMPDC)."}

@mcp.tool(name="workplace_wellness_guide", description="Guidance for employers and employees on mental health at work in Kenya: the employer's duty of care, employee assistance programmes, stress and sick leave, burnout, policies and reducing stigma. Use when someone asks what an employer should or must do. Keywords in query select entries; if none match, ALL guidance is returned. Returns the source label, the matching guidance and a DOSHS pointer. A summary labelled DEMO: programme costs and leave rules are indicative, so confirm with DOSHS and the Employment Act. Read-only; no side effects.", annotations=READ_ONLY)
def workplace_wellness_guide(query: Annotated[str | None, Field(description="Optional topic such as eap, stress_leave or policies.")] = None) -> dict:
    INFO = {
        "legal_obligation": "Employers have duty of care under Occupational Safety & Health Act 2007. Mental health included.",
        "eap":              "Employee Assistance Programs: Chiromo Lane, Minet Kenya, UAP Old Mutual offer EAP packages. Cost: KES 500-2000/employee/year.",
        "stress_leave":     "No specific 'mental health leave' in Kenya law. Use sick leave (7 days statutory). Doctor's note required.",
        "burnout_guide":    "Burnout is not a medical diagnosis in Kenya yet. Manage as occupational stress under OSHA.",
        "policies":         "Create mental health policy: awareness, confidentiality, accommodation, EAP, manager training.",
        "reduce_stigma":    "Training managers to recognize signs. Anonymous wellness surveys. Normalise 'mental health days'.",
    }
    if query:
        q = query.lower()
        matched = {k: v for k, v in INFO.items() if k in q or any(w in q for w in k.split("_"))}
        return {"source": "DEMO — DOSH Kenya, DOSHS", "query": query, "guidance": matched or INFO}
    return {"source": "DEMO — Kenya Occupational Safety & Health Act 2007", "guidance": INFO,
            "dosh": "Directorate of Occupational Safety and Health Services: doshs.go.ke"}

@mcp.tool(name="self_help_resources", description="Kenyan mental health self-help resources: online sources, support groups and self-care ideas, with when to seek professional help. Use when someone wants peer support or self-care options rather than a clinic. area is only echoed back; the same list is returned for everyone. Returns the source label, online resources, support groups, self-care suggestions and a when-to-seek-help note. A short list labelled DEMO and not an endorsement: self-help does not replace professional care, and for a crisis use crisis_line_directory. Read-only; no side effects.", annotations=READ_ONLY)
def self_help_resources(area: Annotated[str | None, Field(description="Optional area; only echoed back.")] = None) -> dict:
    return {"source": "DEMO — Kenya mental health organizations", "area": area,
            "online_resources": [
                {"name": "Niskize", "url": "niskize.com", "description": "Kenya mental health awareness, articles, provider directory"},
                {"name": "WHO Mental Health Atlas Kenya", "url": "who.int", "description": "Country-level mental health data"},
            ],
            "support_groups": [
                {"name": "Anxiety & Depression Support Kenya", "platform": "Facebook (private group)",
                 "description": "Peer support community"},
                {"name": "KCPA Patient Support", "description": "Kenya Psychiatric Association patient forums"},
                {"name": "AA Kenya", "description": "Alcoholics Anonymous Kenya: aaKenya.org"},
            ],
            "self_care": ["Regular exercise (even 20-min walk reduces anxiety)", "Sleep hygiene",
                          "Social connection — invest in 2-3 strong relationships",
                          "Limit social media consumption during stressful periods",
                          "Mindfulness: Headspace/Calm apps available free tier"],
            "when_to_seek_help": "Seek professional help if symptoms persist 2+ weeks or significantly affect daily functioning."}

def main() -> None:
    """Console entry point."""
    mcp.run()
