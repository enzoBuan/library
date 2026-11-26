from odoo import fields, models


class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"

    name = fields.Char(string="Name", required=True)

    _sql_constraints = [
        (
            "name_unique",
            "UNIQUE(name)",
            "A book category with this name already exists.",
        ),
    ]
