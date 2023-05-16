import { useState, useEffect } from 'react';
import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8080/',
  timeout: 1000,
});

function App() {
  const [catalog, setCatalog] = useState();
  useEffect(() => {
    instance.get('getCatalog').then(function (response) {
      setCatalog(response.data);
    });
  }, []);

  return (
    <div>
      <form
        action="http://localhost:8080/add_order"
        method="post"
        style={{
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          maxWidth: 500,
        }}
      >
        <label for="customerName">Customer Name:</label>
        <input type="text" id="customerName" name="customerName" required />

        <label for="customerPhone">Customer Phone:</label>
        <input type="text" id="customerPhone" name="customerPhone" required />

        <label for="deliveryAddress">Delivery Address:</label>
        <input
          type="text"
          id="deliveryAddress"
          name="deliveryAddress"
          required
        />

        <label for="areaCode">Delivery Area Code:</label>
        <input type="text" id="areaCode" name="areaCode" required />

        <label for="foodItem">Food Item:</label>
        <select id="foodItem" name="foodItem" required>
          {catalog
            ? catalog.map(({ name, price }) => (
                <option value={name}>{`${name}- ${price}`}</option>
              ))
            : 'No Options'}
        </select>

        <label for="orderType">Order Type:</label>
        <select id="orderType" name="orderType" required>
          <option value="online">Online</option>
          <option value="phone">Phone</option>
        </select>

        <label for="paymentMode">Payment Mode:</label>
        <select id="paymentMode" name="paymentMode" required>
          <option value="cash">Cash</option>
          <option value="creditCard">Credit Card</option>
          <option value="debitCard">Debit Card</option>
        </select>

        <label for="paymentDetails">Payment Details:</label>
        <textarea
          id="paymentDetails"
          name="paymentDetails"
          rows="4"
          cols="50"
        ></textarea>

        <input type="submit" value="Place Order" />
      </form>
    </div>
  );
}

export default App;
