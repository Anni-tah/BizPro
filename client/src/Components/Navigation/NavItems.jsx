import React from "react";
import { Home, User, MessageSquare, CreditCard } from "lucide-react";

const NavItems = [
  { label: "Home", to: "/", icon: <Home size={18} /> },
  { label: "Features", to: "/features", icon: <User size={18} /> },
  { label: "Contact", to: "/contact", icon: <MessageSquare size={18} /> },
  { label: "Pricing", to: "/pricing", icon: <CreditCard size={18} /> },
];

export default NavItems;