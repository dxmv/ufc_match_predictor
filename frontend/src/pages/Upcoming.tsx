import React from 'react';
import EventPage from './EventPage';
import { UFCEvent } from '../types/match_types';

const Upcoming: React.FC = () => {
    const event: UFCEvent = {
        name: "UFC 310",
        date: "2024-12-14",
        location: "Las Vegas, NV",
        matches: [{
            id: "1",
            red_fighter: { id: "1", name: "John Doe"},
            blue_fighter: { id: "2", name: "Jane Doe"},
            red_odds: +500,
            blue_odds: -200,
        },{
            id: "1",
            red_fighter: { id: "1", name: "John Doe"},
            blue_fighter: { id: "2", name: "Jane Doe"},
            red_odds: +500,
            blue_odds: -200,
        }]
    };

    return (
        <EventPage event={event} />
    );
};

export default Upcoming;