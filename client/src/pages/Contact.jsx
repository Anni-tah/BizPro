import React from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import contactSchema from "../schemas/contactSchema";

import InputField from "../Components/forms/InputField";
import TextArea from "../Components/forms/TextArea";
import Button from "../Components/forms/Button";



const Contact = () => {
    const {
        register,
        handleSubmit,
        formState: { errors, isSubmitting },
    } = useForm({
        resolver: zodResolver(contactSchema),
    });

    const onSubmit = async (data) => {
        console.log("Form submitted:", data);
        // send to backend
    };

    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-[#2d2d2d] px-4">
            <form
                onSubmit={handleSubmit(onSubmit)}
                className="bg-[#e8e7e3] p-8 rounded-lg shadow-md w-full max-w-md"
            >
                <h2 className="text-2xl font-bold mb-6 text-[#525333]">Contact Us</h2>

                <InputField
                    label="Name"
                    name="name"
                    type="text"
                    placeholder="Enter your name"
                    register={register}
                    error={errors.name}
                />

                <InputField
                    label="Email"
                    name="email"
                    type="email"
                    placeholder="Enter your email"
                    register={register}
                    error={errors.email}
                />

                <TextArea
                    label="Message"
                    name="message"
                    placeholder="Enter your message"
                    register={register}
                    error={errors.message}
                />

                <Button
                    type="submit"
                    className="w-full bg-[#525333] text-white mt-4 py-2 px-4 rounded hover:bg-[#b8723e] transition-colors duration-300 focus:outline-none focus:ring-2 focus:ring-[#cf8852] focus:ring-opacity-50"
                    disabled={isSubmitting}
                >
                    {isSubmitting ? "Sending..." : "Send Message"}
                </Button>
            </form>
        </div>
    );
}
export default Contact;