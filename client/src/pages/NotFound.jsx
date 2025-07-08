import React from "react";
import { Link } from "react-router-dom";

function NotFound() {
    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
            <h1 className="text-6xl font-bold text-gray-800">404</h1>
            <p className="mt-4 text-lg text-gray-600">Page Not Found</p>
            <Link
                to="/"
                className="mt-6 text-blue-500 hover:underline text-lg transition duration-300"
            >
                Go to Home
            </Link>
        </div>
    );
}

export default NotFound;
