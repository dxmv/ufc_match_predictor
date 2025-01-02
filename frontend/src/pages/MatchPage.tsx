import React, { useEffect, useState } from 'react';
import { Match } from "../types/match_types";
import { fetchUpcomingMatch, fetchPreviousMatch } from "../services/api/matchesApi";

const MatchPage = ({ matchId, upcoming = false }: { matchId: string, upcoming: boolean }) => {
    const [match, setMatch] = useState<Match | null>(null);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchMatch = async () => {
            try {
                const matchData = upcoming ? await fetchUpcomingMatch(matchId) : await fetchPreviousMatch(matchId);
                setMatch(matchData);
            } catch (err) {
                setError("Failed to fetch match data");
            }
        };

        fetchMatch();
    }, [matchId, upcoming]);

    if (error) {
        return <div className="min-h-screen flex items-center justify-center">{error}</div>;
    }

    if (!match) {
        return <div className="min-h-screen flex items-center justify-center">Loading...</div>;
    }

    return (
        <div className="min-h-screen">
            {/* Official background image */}
            <div className="relative h-96 bg-cover bg-center mb-10" style={{ backgroundImage: `url(https://dmxg5wxfqgb4u.cloudfront.net/styles/background_image_xl/s3/2024-11/120724-ufc-310-pantoja-vs-asakura-EVENT-ART.jpg?h=d1cb525d&itok=XWZWovZk)` }}>
                {/* Black overlay */}
                <div className="absolute top-0 left-0 w-full h-full bg-black opacity-60 flex flex-col justify-center items-center">
                    <h1 className="text-white text-5xl font-bold mt-10">{match.red_fighter.name} vs {match.blue_fighter.name}</h1>
                    <p className="text-white text-lg mt-5">{match.id}</p>
                </div>
            </div>
            {/* Match details */}
            <div className="container mx-auto px-4">
                <h2 className="text-3xl font-bold mb-4">Match Details</h2>
                <p>Red Fighter: {match.red_fighter.name}</p>
                <p>Blue Fighter: {match.blue_fighter.name}</p>
                <p>Red Odds: {match.red_odds}</p>
                <p>Blue Odds: {match.blue_odds}</p>
                <p>Winner: {match.winner}</p>
                {match.predicted && <p>Predicted Winner: {match.predicted}</p>}
            </div>
        </div>
    );
};

export default MatchPage;