def build_sandwich(*items):
    """Build a sandwich with items the client wants."""
    print("\nBuilding the sandwich with:")
    for item in items:
        print(f"-{item}")


build_sandwich("ham")
build_sandwich("tomatoe", "lettuce")
build_sandwich("cheese", "mushrooms", "turkey")
