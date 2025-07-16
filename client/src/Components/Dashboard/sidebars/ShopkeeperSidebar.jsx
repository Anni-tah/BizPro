import React from 'react';
const ShopkeeperSidebar = () => (
    <div className="h-full p-4">
      <h2 className="text-white text-lg font-bold mb-6">BizPro</h2>
      <ul className="space-y-3">
        <li className="font-semibold text-sm text-white uppercase">Dashboard</li>
        <li><a href="#" className="hover:text-blue-light">Customer Orders</a></li>
        <li><a href="#" className="hover:text-blue-light">Products</a></li>
        <li><a href="#" className="hover:text-blue-light">Inventory</a></li>
        <li><a href="#" className="hover:text-blue-light">Customer Payment</a></li>
        <li><a href="#" className="hover:text-blue-light">Reports</a></li>
      </ul>
    </div>
  );
  
  export default ShopkeeperSidebar;
  