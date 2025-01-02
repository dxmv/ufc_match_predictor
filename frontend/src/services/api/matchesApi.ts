import { Match, Fighter } from "../../types/match_types";

const BACKEND_URL = "http://127.0.0.1:5000";

/**
 * Maps raw match data to the Match type
 * @param rawMatch The raw match data
 * @returns A Match object
 */
const mapToMatchType = (rawMatch: any): Match => {
    console.log(rawMatch);
    const redFighter: Fighter = { id: 'red', name: rawMatch.RedFighter, image_link: rawMatch.RedFighterImage };
    const blueFighter: Fighter = { id: 'blue', name: rawMatch.BlueFighter, image_link: rawMatch.BlueFighterImage };

    return {
        id: `${rawMatch.Date}-${rawMatch.RedFighter}-${rawMatch.BlueFighter}`, // Example ID
        red_fighter: redFighter,
        blue_fighter: blueFighter,
        red_odds: rawMatch.RedOdds,
        blue_odds: rawMatch.BlueOdds,
        winner: rawMatch.Winner,
        predicted: rawMatch.predicted == 1 ? "Red" : "Blue",
    };
};

/**
 * Fetches the previous matches from the backend
 * @returns An array of Match objects
 */
export const fetchPreviousMatches = async (page?: number,per_page?: number): Promise<Array<Match>> => {
    const response = await fetch(`${BACKEND_URL}/previous?page=${page}&per_page=${per_page}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    });
    const data = await response.json();

    // Map the incoming data to the Match type
    return data.map(mapToMatchType);
};

/**
 * Fetches the upcoming matches from the backend
 * @returns An array of Match objects
 */
export const fetchUpcomingMatches = async (): Promise<Array<Match>> => {
    const response = await fetch(`${BACKEND_URL}/upcoming`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    });
    const data = await response.json();

    // Map the incoming data to the Match type
    return data.map(mapToMatchType);
};

/**
 * Fetches the accuracy of the model from the backend
 * @returns The accuracy of the model
 */
export const fetchAccuracy = async (): Promise<number> => {
    const response = await fetch(`${BACKEND_URL}/accuracy`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    });
    const data = await response.json();
    return data.accuracy;
};