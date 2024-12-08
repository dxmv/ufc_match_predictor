export interface Fighter {
    id: string;
    name: string;
}

export interface Match {
    id: string;
    red_fighter: Fighter;
    blue_fighter: Fighter;
    red_odds: number;
    blue_odds: number;
}

export interface UFCEvent {
    name: string;
    date: string;
    location: string;
    matches: Match[];
}
