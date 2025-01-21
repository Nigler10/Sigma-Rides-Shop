console.log("Javascript here")

document.getElementById("image").addEventListener("mouseover", function() {
    var gifPath = document.getElementById("gifPath").value;
    this.src = gifPath;
});

document.getElementById("image").addEventListener("mouseout", function() {
    var imagePath = document.getElementById("imagePath").value;
    this.src = imagePath;
});



// let cart = {};
//
// function addToCart(productName, price) {
//   if (cart[productName]) {
//     cart[productName].quantity += 1;
//   } else {
//     cart[productName] = {
//       price: price,
//       quantity: 1
//     };
//   }
//   displayCart();
// }
//
// function removeFromCart(productName) {
//   delete cart[productName];
//   displayCart();
// }
//
// function updateQuantity(productName, quantity) {
//   if (quantity < 1) {
//     quantity = 1;
//   }
//   cart[productName].quantity = parseInt(quantity);
//   displayCart();
// }
//
// function displayCart() {
//   const cartContainer = document.getElementById('cart');
//   const totalContainer = document.getElementById('total');
//   cartContainer.innerHTML = '';
//
//   let totalPrice = 0;
//   for (const productName in cart) {
//     const item = cart[productName];
//     const itemPrice = item.price * item.quantity;
//     totalPrice += itemPrice;
//
//     const cartItem = document.createElement('div');
//     cartItem.className = 'cart-item';
//     cartItem.innerHTML = `
//       <span>${productName}</span>
//       <input type="number" value="${item.quantity}" min="1" onchange="updateQuantity('${productName}', this.value)">
//       <span class="item-price">$${itemPrice}</span>
//       <button class="btn" onclick="removeFromCart('${productName}')">Remove</button>
//     `;
//
//     cartContainer.appendChild(cartItem);
//   }
//
//   totalContainer.textContent = `Total: $${totalPrice}`;
// }
//
// function buy() {
//    if (confirm("Purchase it now?") == true) {
//         alert('Thank you for your purchase!');
//     } else {
//         alert('Understable, Have a Great Day!');
//     }
// }
