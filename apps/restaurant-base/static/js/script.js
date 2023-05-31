function showReport() {
  var date1Input = document.getElementById('date1');
  var date2Input = document.getElementById('date2');

  var date1Value = date1Input.value;
  var date2Value = date2Input.value;

  console.log('Date 1:', date1Value);
  console.log('Date 2:', date2Value);

  const startDate = new Date(date1Value);
  const endDate = new Date(date2Value);

  fetch('/api/order_endpoint')
    .then((res) => res.json())
    .then((res) => {
      console.log(res);
      var reportElement = document.getElementById('report');
      reportElement.innerHTML = '';

      var paragraphInfo = document.createElement('p');
      paragraphInfo.textContent =
        'This report contains all orders form ' +
        date1Value +
        ' to ' +
        date2Value +
        '.';
      reportElement.appendChild(paragraphInfo);
      reportElement.classList.toggle('show');

      var table = document.createElement('table');
      const orders = res.order;
      const foodItems = res.foodItems;
      const orderItems = res.orderItems;
      const customers = res.customers;

      var header = document.createElement('tr');
      Object.keys(orders[0]).forEach((key) => {
        var keyCell = document.createElement('td');
        keyCell.textContent = key;
        keyCell.className = key;
        header.appendChild(keyCell);
      });
      var keyCell = document.createElement('td');
      keyCell.textContent = 'dishes';
      keyCell.className = 'dishes';
      header.appendChild(keyCell);
      var keyCell = document.createElement('td');
      keyCell.textContent = 'price';
      keyCell.className = 'price';
      header.appendChild(keyCell);

      table.appendChild(header);
      orders
        .filter((order) => {
          const objDate = new Date(order.date);
          return objDate >= startDate && objDate <= endDate;
        })
        .sort((a, b) => {
          const dateA = new Date(a.date);
          const dateB = new Date(b.date);
          if (dateA.getTime() === dateB.getTime()) {
            const customerA = customers.filter(
              (customer) => customer.id === a.customer_id
            )[0].name;
            const customerB = customers.filter(
              (customer) => customer.id === b.customer_id
            )[0].name;
            return customerA.localeCompare(customerB);
          }
          return dateA - dateB;
        })


        .forEach((order) => {
          var row = document.createElement('tr');

          var keyCell = document.createElement('td');
          keyCell.textContent = order['id'];
          keyCell.className = 'id';
          row.appendChild(keyCell);

          var keyCell = document.createElement('td');
          keyCell.textContent = order['date'].substring(0, 10);
          keyCell.className = 'date';
          row.appendChild(keyCell);

          var keyCell = document.createElement('td');
          keyCell.textContent =
            order['customer_id'] +
            `(${
              customers.filter(
                (customer) => customer.id === order.customer_id
              )[0].name
            })`;
          keyCell.className = 'customer_id';
          row.appendChild(keyCell);

          var keyCell = document.createElement('td');
          keyCell.textContent = order['employee_id'];
          keyCell.className = 'employee_id';
          row.appendChild(keyCell);

          var keyCell = document.createElement('td');
          const names = orderItems
            .filter((item) => item.id === order.id)
            .map((item) => item.itemName);
          keyCell.textContent = String(names);
          keyCell.className = 'dishes';
          row.appendChild(keyCell);

          var keyCell = document.createElement('td');
          console.log(names);
          const price = names
            .map(
              (name) => +foodItems.filter((food) => food.name === name)[0].price
            )
            .reduce((accumulator, currentValue) => {
              return accumulator + currentValue;
            }, 0);
          keyCell.textContent = price;
          keyCell.className = 'price';
          row.appendChild(keyCell);

          table.appendChild(row);
        });

      reportElement.appendChild(table);

      buttonDescriptionElement = document.getElementById('buttonDescription');
      buttonDescriptionElement.textContent = reportElement.classList.contains(
        'show'
      )
        ? 'Hide'
        : 'Submit';
    });
}
