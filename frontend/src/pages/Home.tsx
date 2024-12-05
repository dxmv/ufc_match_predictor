/**
 * Here we should describe what the app does.
 * What it is for, what it is about.
 * How does the user use the app?
 * How do we get the predictions?
 */
import React from 'react';

const Home: React.FC = () => {
    return (
        <div className="min-h-screen">
            {/* Hero Section */}
            <div className="bg-blue-600 text-white py-16">
                <div className="container mx-auto px-4 text-center">
                    <h1 className="text-5xl font-bold mb-4">UFC Fight Predictor</h1>
                    <p className="text-xl mb-8 max-w-2xl mx-auto">
                        Get data-driven predictions for upcoming UFC fights using advanced analytics
                    </p>
                    <button className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold 
                        hover:bg-blue-50 transition duration-300">
                        View Upcoming Predictions
                    </button>
                </div>
            </div>

            {/* Features Section */}
            <div className="py-16 container mx-auto px-4">
                <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                    {/* Feature 1 */}
                    <div className="bg-white p-6 rounded-xl shadow-lg">
                        <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
                            <svg className="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} 
                                    d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                            </svg>
                        </div>
                        <h3 className="text-xl font-semibold mb-2">Advanced Analytics</h3>
                        <p className="text-gray-600">
                            Our predictions are based on comprehensive fighter statistics, historical performance, 
                            and machine learning algorithms.
                        </p>
                    </div>

                    {/* Feature 2 */}
                    <div className="bg-white p-6 rounded-xl shadow-lg">
                        <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
                            <svg className="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} 
                                    d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                        </div>
                        <h3 className="text-xl font-semibold mb-2">Real-time Updates</h3>
                        <p className="text-gray-600">
                            Stay up to date with the latest predictions for upcoming UFC events and fight cards.
                        </p>
                    </div>

                    {/* Feature 3 */}
                    <div className="bg-white p-6 rounded-xl shadow-lg">
                        <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
                            <svg className="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} 
                                    d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                            </svg>
                        </div>
                        <h3 className="text-xl font-semibold mb-2">Success Rate</h3>
                        <p className="text-gray-600">
                            Track our prediction accuracy and make informed decisions based on our historical success rate.
                        </p>
                    </div>
                </div>
            </div>

            {/* How It Works Section */}
            <div className="bg-gray-50 py-16">
                <div className="container mx-auto px-4">
                    <h2 className="text-3xl font-bold text-center mb-12">How It Works</h2>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto">
                        <div className="text-center">
                            <div className="w-12 h-12 bg-blue-600 text-white rounded-full flex items-center 
                                justify-center text-xl font-bold mx-auto mb-4">
                                1
                            </div>
                            <p className="text-gray-700">Select an upcoming UFC event</p>
                        </div>
                        <div className="text-center">
                            <div className="w-12 h-12 bg-blue-600 text-white rounded-full flex items-center 
                                justify-center text-xl font-bold mx-auto mb-4">
                                2
                            </div>
                            <p className="text-gray-700">View detailed fighter analysis</p>
                        </div>
                        <div className="text-center">
                            <div className="w-12 h-12 bg-blue-600 text-white rounded-full flex items-center 
                                justify-center text-xl font-bold mx-auto mb-4">
                                3
                            </div>
                            <p className="text-gray-700">Get fight outcome predictions</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Home;