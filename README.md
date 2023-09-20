# Colonel-Blotto
## GAME RULES
Each player has 5 troops and can send these troops to any of the three 3 battlefields (this can easily be adjusted but this is the way it's currently set up). All troops must be sent and as many or as few troops can be sent to each battlefield as the player desires as long as it is not more than 5 or less than 0. Whichever side has more troops present on a particular battlefield is considered the winner of that battle. The margin of victory does not matter. The player who wins the most battles whether it be win 1 tie 2 or win 2 lose 1, wins the game. The goal is to find the optimal strategy and reach a Nash equilibrium so that even if the opposing player knew our strategy no player would have incentive to deviate from the strategy. We do this by finding the optimal mixed strategy and assigning a probability of chosing a given strategy. Strategies are represented as so: (1,3,1) meaning one soldier at battlfield 1 3 soldiers on battlfield 2 and 1 soldier on battlefield 3.

## Solving The Colonel Blotto Game theory Problem
Currently only the naive solution is in the repo. Hoping to add more as I learn more and not only impliment a more efficient less brute force algorithm but also add a larger version of the game.

Note that currently I differntiate options that are technically the same for example (0,2,3) is distinct from (2,3,0). Technically (2,3,0) is correct in any form (note (4,1,0) in all it's forms is not a statisfactory exploit and will lose in the long run) but to compute it's sucess in a game vs all strategies you would to the best of my knoweldge need all of it's permutations to determine it's sucess against other strategies. 

GAME DESCRIPTION: https://en.wikipedia.org/wiki/Blotto_game
