from printing_functions import print_models
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_models)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
complete = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

