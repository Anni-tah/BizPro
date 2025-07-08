import React from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import signupSchema from "../../schemas/signupSchema";
import PasswordField from "../../Components/forms/PasswordField";
import InputField from "../../Components/forms/InputField";
import SelectField from "../../Components/forms/SelectField";
import Button from "../../Components/forms/Button";

const SignUp = () => {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm({
    resolver: zodResolver(signupSchema),
  });

  const onSubmit = async (data) => {
    try {
      const response = await fetch("http://localhost:5000/users", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: data.username,
          email: data.email,
          role: data.role,
          password: data.password,
        }),
      });

      if (!response.ok) {
        throw new Error("Sign up failed");
      }

      const result = await response.json();
      console.log("Sign up successful:", result);
      alert("Sign up successful! Please log in.");
      window.location.href = "/login";
    } catch (error) {
      console.error("Error during sign up:", error);
      if (error.message === "Sign up failed") {
        alert("Sign up failed. Please check your details and try again.");
      } else {
        alert("An unexpected error occurred. Please try again later.");
      }
    }
  };

  const roleOptions = [
    { value: "admin", label: "Admin" },
    { value: "storekeeper", label: "Storekeeper" },
    { value: "customer", label: "Customer" },
    { value: "supplier", label: "Supplier" },
  ];

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-[#2d2d2d] px-4">
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="bg-[#e8e7e3] p-8 rounded-lg shadow-md w-full max-w-md"
      >
        <h2 className="text-2xl font-bold mb-6 text-[#525333]">Sign Up</h2>

        <InputField
          label="Username"
          name="username"
          type="text"
          placeholder="Enter your username"
          register={register}
          error={errors.username}
        />

        <InputField
          label="Email"
          name="email"
          type="email"
          placeholder="Enter your email"
          register={register}
          error={errors.email}
        />

        <SelectField
          name="role"
          label="Role"
          options={roleOptions}
          register={register}
          error={errors.role}
        />

        <PasswordField
          label="Password"
          name="password"
          register={register}
          error={errors.password}
          placeholder="Enter your password"
        />

        <PasswordField
          label="Confirm Password"
          name="confirmPassword"
          register={register}
          error={errors.confirmPassword}
          placeholder="Confirm your password"
        />

        <Button
          type="submit"
          disabled={isSubmitting}
          className={`w-full p-2 px-4 bg-[#525333] text-white mt-4 hover:bg-[#b8723e] focus:outline-none focus:ring-2 focus:ring-[#cf8852] ${
            isSubmitting ? "opacity-50 cursor-not-allowed" : ""
          }`}
        >
          {isSubmitting ? "Signing up..." : "Sign Up"}
        </Button>

        <div className="mt-4 text-center text-sm text-[#525333]">
          Already have an account?{" "}
          <a href="/login" className="text-[#b8723e] hover:underline">
            Login
          </a>
        </div>
      </form>
    </div>
  );
};

export default SignUp;
