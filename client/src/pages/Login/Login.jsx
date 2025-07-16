import React, { useState } from "react";
import { useForm } from "react-hook-form";  
import { zodResolver } from "@hookform/resolvers/zod";
import loginSchema from "../../schemas/loginSchema";
import PasswordField from "../../Components/forms/PasswordField";
import InputField from "../../Components/forms/InputField";
import Button from "../../Components/forms/Button";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [errorMessage, setErrorMessage] = useState(null);
  const navigate = useNavigate();

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm({
    resolver: zodResolver(loginSchema),
  });

  const onSubmit = async (data) => {
    try {
      const response = await fetch("http://localhost:5000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        const err = await response.json();
        throw new Error(err.message || "Login failed");
      }

      const result = await response.json();
      localStorage.setItem("access_token", result.access_token);
      localStorage.setItem("user", JSON.stringify(result.user));

      // ✅ Redirect based on role
      const role = result.user?.role;
      navigate(`/dashboard/${role}`);
    } catch (error) {
      console.error("Error during login:", error);
      setErrorMessage("Login failed. Please check your credentials and try again.");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-brick px-4">
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="bg-gray p-8 rounded-lg shadow-md w-full max-w-md"
      >
        <h2 className="text-2xl font-bold mb-6 text-blue">Login</h2>

        <InputField
          label="Email"
          name="email"
          type="email"
          placeholder="Enter your email"
          register={register}
          error={errors.email}
        />

        <PasswordField
          label="Password"
          name="password"
          register={register}
          errors={errors}
          placeholder="Enter your password"
        />

        <Button
          type="submit"
          className="w-full mt-4 py-2 px-4 rounded bg-blue text-white hover:bg-blue-light transition-colors duration-300"
          disabled={isSubmitting}
        >
          {isSubmitting ? "Logging in..." : "Login"}
        </Button>

        {errorMessage && (
          <p className="text-brick-red text-sm mt-3 text-center">
            {errorMessage}
          </p>
        )}

        <div className="mt-4 text-center text-sm text-blue">
          Don't have an account?{" "}
          <a href="/signup" className="text-blue-light hover:underline">
            Sign Up
          </a>
        </div>
      </form>
    </div>
  );
};

export default Login;
