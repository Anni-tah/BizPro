import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Layout from "../Components/Dashboard/Layout";

// Import dashboards for each role
import CustomerMainDashboard from "./Dashboard/Customer/CustomerMainSidebar";
// import AdminMainDashboard from "./Dashboard/Admin/AdminMainDashboard";
// import ShopkeeperMainDashboard from "./Dashboard/Shopkeeper/ShopkeeperMainDashboard";
 import SupplierMainDashboard from "./Dashboard/SupplierMainDashboard";
 import AdminHomeDashboard from "./Dashboard/Admin/AdminHomeDashboard";

const Dashboard = () => {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();
  const { role } = useParams();

  useEffect(() => {
    const storedUser = localStorage.getItem("user");
    if (!storedUser) {
      navigate("/login");
      return;
    }

    const parsedUser = JSON.parse(storedUser);
    if (parsedUser.role !== role) {
      navigate(`/dashboard/${parsedUser.role}`);
      return;
    }

    setUser(parsedUser);
  }, [navigate, role]);

  if (!user) return null;

  // Load correct dashboard based on role
  let DashboardContent = null;

  if (role === "customer") {
    DashboardContent = <CustomerMainDashboard />;
  }
   if (role === "admin") DashboardContent = <AdminHomeDashboard />;
  // else if (role === "shopkeeper") DashboardContent = <ShopkeeperMainDashboard />;
   else if (role === "supplier") DashboardContent = <SupplierMainDashboard />;

  return <Layout user={user}>{DashboardContent}</Layout>;
};

export default Dashboard;
