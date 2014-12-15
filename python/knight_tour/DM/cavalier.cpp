#include <iostream>
#include <string>
#include <random>

struct Position
{
    int x, y;
};

unsigned N = 6;
std::vector<Position> HISTORIQUE;

void afficher(const Position& last_move={0, 0})
{
    std::vector<std::string> liste{N*N, " ."};
    int x, y;
    for(unsigned i = 0; i < HISTORIQUE.size(); ++i)
    {
        auto pos = HISTORIQUE[i];
        x = pos.x;
        y = pos.y;
        liste[x + y * N] = std::to_string(i);
    }
    if(last_move.x != 0 || last_move.y != 0)
    {
        int last_x = x + last_move.x;
        int last_y = y + last_move.y;
        liste[last_x + last_y * N] = " :";
    }

    std::string espace{15, '\n'};
    std::string titre = "TOUR "
                      + std::to_string(HISTORIQUE.size())
                      + ". Cavalier en ("
                      + std::to_string(x)
                      + ", "
                      + std::to_string(y)
                      + ").\n\n";
    std::string L1 = " " + 
}
