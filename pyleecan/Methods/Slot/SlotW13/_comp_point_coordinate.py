from numpy import arcsin, exp, tan


def _comp_point_coordinate(self):
    """Compute the point coordinates needed to plot the Slot.

    Parameters
    ----------
    self : SlotW13
        A SlotW13 object

    Returns
    -------
    point_list: list
        A list of  10 Points

    """
    Rbo = self.get_Rbo()

    if self.H1_is_rad:  # H1 in rad
        H1 = ((self.W1 - self.W0) / 2.0) * tan(self.H1)  # convertion to m
    else:  # H1 in m
        H1 = self.H1

    # alpha is the angle to rotate Z0 so ||Z1,Z10|| = W0
    alpha = float(arcsin(self.W0 / (2 * Rbo)))

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(1j * alpha)

    if self.is_outwards():
        Z2 = Z1 + self.H0
        Z3 = Z2 + H1 + (self.W1 - self.W0) * 1j / 2.0
        Z4 = Z3 - (self.W1 - self.W2) / 2.0 * 1j
        Z5 = Z4 + self.H2 + (self.W3 - self.W2) / 2.0 * 1j
    else:  # inward slot
        Z2 = Z1 - self.H0
        Z3 = Z2 - H1 + (self.W1 - self.W0) * 1j / 2.0
        Z4 = Z3 - (self.W1 - self.W2) / 2.0 * 1j
        Z5 = Z4 - self.H2 + (self.W3 - self.W2) / 2.0 * 1j

    # symetry
    Z6 = Z5.conjugate()
    Z7 = Z4.conjugate()
    Z8 = Z3.conjugate()
    Z9 = Z2.conjugate()
    Z10 = Z1.conjugate()
    return [Z10, Z9, Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1]
