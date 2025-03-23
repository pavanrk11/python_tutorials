class CheckoutState:
    def add_item(self, item):
        pass

    def review_cart(self):
        pass

    def enter_shipping_info(self, info):
        pass

    def process_payment(self):
        pass


class EmptyCartState(CheckoutState):
    def add_item(self, item):
        print("Item added to the cart.")
        return ItemAddedState()

    def review_cart(self):
        print("Cannot review an empty cart.")

    def enter_shipping_info(self, info):
        print("Cannot enter shipping info with an empty cart.")

    def process_payment(self):
        print("Cannot process payment with an empty cart.")


class ItemAddedState(CheckoutState):
    def add_item(self, item):
        print("Item added to the cart.")

    def review_cart(self):
        print("Reviewing cart contents.")
        return CartReviewedState()

    def enter_shipping_info(self, info):
        print("Cannot enter shipping info without reviewing the cart.")

    def process_payment(self):
        print("Cannot process payment without entering shipping info.")


class CartReviewedState(CheckoutState):
    def add_item(self, item):
        print("Cannot add items after reviewing the cart.")

    def review_cart(self):
        print("Cart already reviewed.")

    def enter_shipping_info(self, info):
        print("Entering shipping information.")
        return ShippingInfoEnteredState()

    def process_payment(self):
        print("Cannot process payment without entering shipping info.")


class ShippingInfoEnteredState(CheckoutState):
    def add_item(self, item):
        print("Cannot add items after entering shipping info.")

    def review_cart(self):
        print("Cannot review cart after entering shipping info.")

    def enter_shipping_info(self, info):
        print("Shipping information already entered.")

    def process_payment(self):
        print("Processing payment with the entered shipping info.")


class CheckoutContext:
    def __init__(self):
        self.current_state = EmptyCartState()

    def add_item(self, item):
        self.current_state = self.current_state.add_item(item)

    def review_cart(self):
        self.current_state = self.current_state.review_cart()

    def enter_shipping_info(self, info):
        self.current_state = self.current_state.enter_shipping_info(info)

    def process_payment(self):
        self.current_state.process_payment()

if __name__ == "__main__":
    cart = CheckoutContext()

    cart.add_item("iphone")
    cart.review_cart()
    cart.enter_shipping_info("259, BSK stage 3, Bengaluru")
    cart.process_payment()