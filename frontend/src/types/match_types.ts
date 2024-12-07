interface Fighter {
    id: string;
    name: string;
    image_url: string;
}

interface Match {
    id: string;
    red_fighter: Fighter;
    blue_fighter: Fighter;
    red_odds: number;
    blue_odds: number;
}

export type { Fighter, Match };