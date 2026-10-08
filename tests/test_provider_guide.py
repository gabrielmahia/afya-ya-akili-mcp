from afya_ya_akili_mcp import server


def test_the_provider_finder_returns_the_provider_type_guide():
    """TYPES (what each kind of provider does) was built on every call and never returned."""
    fn = server.mental_health_provider_finder
    r = (fn.fn if hasattr(fn, "fn") else fn)()
    assert set(r["provider_type_guide"]) == {"psychiatrist", "psychologist", "counselor", "psychotherapist"}
