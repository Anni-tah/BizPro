import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { signupSchema } from "../../schemas/signupSchema";
import PasswordField from "../../Components/forms/PasswordField";
import InputField from "../../Components/forms/InputField";
import SelectField from "../../Components/forms/SelectField";
import Button from "../../Components/Button";

const SignUp = () => {
    const {
        register,
        handleSubmit,
        formState: { errors, isSubmitting },
    } = useForm({
        resolver: zodResolver(signupSchema),
    });

    const onSubmit = async (data) => {
        console.log("Form submitted:", data);
        // send to backend
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
