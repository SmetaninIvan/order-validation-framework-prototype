import allure
from pages.order_page import OrderPage

@allure.feature("Order flow")
def test_order_flow(driver, db, order_processor):
    order_name = "test_order_1"

    page = OrderPage(driver, db)

    page.create_order(order_name)

    assert db.get_order_status(order_name) == "New"

    order_processor.prepare_order(order_name)

    assert db.get_order_status(order_name) == "Ready"