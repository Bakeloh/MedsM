import click
from models import User, Medicine
from datetime import datetime

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Name', help='Name of the medicine')
@click.option('--category', prompt='Category', help='Category of the medicine')
@click.option('--quantity', prompt='Quantity', type=int, help='Quantity of the medicine')
@click.option('--expiry-date', prompt='Expiry Date (YYYY-MM-DD)', help='Expiry date of the medicine')
def add_medicine(name, category, quantity, expiry_date):
    """Add a new medicine."""
    expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d').date()
    Medicine.add_medicine(name, category, quantity, expiry_date)
    click.echo(f"Medicine '{name}' added successfully.")

@cli.command()
@click.argument('search_term')
def search_medicines(search_term):
    """Search for medicines."""
    medicines = Medicine.search_medicines(search_term)
    if medicines:
        click.echo(f"Search results for '{search_term}':")
        for medicine in medicines:
            click.echo(medicine)
    else:
        click.echo(f"No medicines found matching '{search_term}'.")

@cli.command()
@click.argument('medicine_id', type=int)
def mark_unavailable(medicine_id):
    """Mark a medicine as unavailable."""
    Medicine.mark_as_unavailable(medicine_id)
    click.echo(f"Medicine with ID {medicine_id} marked as unavailable.")

@cli.command()
def remove_expired():
    """Remove expired medicines."""
    Medicine.remove_expired_medicines()
    click.echo("Expired medicines removed successfully.")
    
    
@cli.command()
@click.argument('username')
def add_user(username):
    """Add a new user."""
    User.add_user(username)
    click.echo(f"User '{username}' added successfully.")


@cli.command()
@click.argument('medicine_id', type=int)
def delete_medicine(medicine_id):
    """Delete a medicine."""
    Medicine.delete_medicine(medicine_id)
    click.echo(f"Medicine with ID {medicine_id} deleted successfully.")


if __name__ == '__main__':
    cli()
