import { Match } from '../../types/match_types';

import MatchCard from './MatchCard';

const MatchList = ({ matches,upcoming }: { matches: Match[],upcoming?:boolean }) => {
    return <div className='flex flex-col items-center justify-center pb-10 px-12 w-100'>{matches.map((match) => <MatchCard match={match} key={match.blue_fighter + " " + match.red_fighter} upcoming={upcoming} />)}</div>;
};

export default MatchList;