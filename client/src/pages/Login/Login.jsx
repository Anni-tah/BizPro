
import { useForm } from "react-hook-form";  
import { zodResolver } from "@hookform/resolvers/zod";
import { loginSchema } from "../../schemas/loginSchema";
import PasswordField from "../../Components/forms/PasswordField";
import InputField from "../../Components/forms/InputField";
import Button from "../../Components/forms/Button";

const Login = () => {
    const {
        register,
        handleSubmit,
        formState: { errors, isSubmitting },
    } = useForm({
        resolver: zodResolver(loginSchema),
    }
    );
    const onSubmit = async (data) => {
        console.log("Form submitted:", data);
        // send to backend
    };
    return(
        <div className="flex flex-col items-center justify-center min-h-screen bg-[#2d2d2d] px-4">
            <form
                onSubmit={handleSubmit(onSubmit)}
                className="bg-[#e8e7e3] p-8 rounded-lg shadow-md w-full max-w-md"
            >
                <h2 className="text-2xl font-bold mb-6 text-[#525333]">Login</h2>

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
                    className="w-full bg-[#525333] text-white mt-4  py-2 px-4 rounded hover:bg-[#b8723e] transition-colors duration-300
                    focus:outline-none focus:ring-2 focus:ring-[#cf8852] focus:ring-opacity-50"
                    disabled={isSubmitting}
                >
                    {isSubmitting ? "Logging in..." : "Login"}
                </Button>

                <div className="mt-4 text-center text-sm text-[#525333]">
                    Don't have an account?{" "}
                    <a href="/signup" className="text-[#b8723e] hover:underline">
                        Sign Up
                    </a>
                </div>

            </form>
        </div>
    );
    }

    
