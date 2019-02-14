Back up data command for Products and Product Conversions:

    python manage.py dumpdata Products.IdProductUnitConv --format json --indent 4 > Products/fixtures/ProductConvData.json

    python manage.py dumpdata Products.IdProduct --format json --indent 4 > Products/fixtures/ProductData.json