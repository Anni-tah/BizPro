import React from "react";

function Cta() {
    return (
        <section className="bg-blue-700 text-white text-center py-16 px-4">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">
                Ready to simplify your business?
            </h2>
            <p className="mb-6 text-lg max-w-xl mx-auto">
                Start using BizPro today and take control of your operations from one smart dashboard.
            </p>
            <a
                href="/signup"
                className="inline-block bg-white text-blue-700 px-6 py-3 rounded-md hover:bg-blue-100 transition"
            >
                Get Started Now
            </a>
        </section>
    );
}

export default Cta;
