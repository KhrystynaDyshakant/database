from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:

    app.register_blueprint(err_handler_bp)

    from .orders.stores_route import stores_bp
    from .orders.products_route import products_bp
    # from.orders.stores_has_products_route import stores_has_products_bp
    from.orders.customers_route import customers_bp
    from.orders.orders_route import orders_bp
    from.orders.city_route import city_bp
    from.orders.street_route import street_bp
    from.orders.location_route import location_bp
    from.orders.delivery_route import delivery_bp
    # from.orders.orders_has_products_route import orders_has_products_bp

    app.register_blueprint(stores_bp)
    app.register_blueprint(products_bp)
    # app.register_blueprint(stores_has_products_bp)
    app.register_blueprint(customers_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(city_bp)
    app.register_blueprint(street_bp)
    app.register_blueprint(location_bp)
    app.register_blueprint(delivery_bp)
    # app.register_blueprint(orders_has_products_bp)
