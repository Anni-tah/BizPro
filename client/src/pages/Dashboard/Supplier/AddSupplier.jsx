import React, { useState } from "react";

const AddSupplier = () => {
  const [formData, setFormData] = useState({
    name: "",
    contact_person: "",
    phone_number: "",
    email: "",
    address: "",
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch("http://localhost:5000/suppliers", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
        credentials: "include", // include cookies if your session is tied to login
      });

      if (res.ok) {
        setMessage("Supplier added successfully!");
        setFormData({
          name: "",
          contact_person: "",
          phone_number: "",
          email: "",
          address: "",
        });
      } else {
        const errorData = await res.json();
        setMessage(errorData.message || "Failed to add supplier.");
      }
    } catch (error) {
      console.error("Error:", error);
      setMessage("Server error. Please try again.");
    }
  };

  return (
    <div className="max-w-md mx-auto p-6 bg-white rounded shadow">
      <h2 className="text-2xl font-bold text-blue mb-4">Add Supplier</h2>

      {message && <div className="mb-4 text-red-500">{message}</div>}

      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          name="name"
          value={formData.name}
          onChange={handleChange}
          placeholder="Company Name"
          required
          className="w-full border p-2 rounded"
        />

        <input
          name="contact_person"
          value={formData.contact_person}
          onChange={handleChange}
          placeholder="Contact Person"
          required
          className="w-full border p-2 rounded"
        />

        <input
          name="phone_number"
          value={formData.phone_number}
          onChange={handleChange}
          placeholder="Phone Number"
          required
          className="w-full border p-2 rounded"
        />

        <input
          name="email"
          type="email"
          value={formData.email}
          onChange={handleChange}
          placeholder="Email"
          required
          className="w-full border p-2 rounded"
        />

        <input
          name="address"
          value={formData.address}
          onChange={handleChange}
          placeholder="Address"
          required
          className="w-full border p-2 rounded"
        />

        <button
          type="submit"
          className="w-full bg-blue text-white py-2 rounded hover:bg-blue-dark"
        >
          Add Supplier
        </button>
      </form>
    </div>
  );
};

export default AddSupplier;
