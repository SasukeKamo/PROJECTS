#define _CRT_SECURE_NO_WARNINGS
#define buffor 40
#define CheckOrPrint 2
#define Check 0
#define Print 1
#define basic 1
#define ifgo 2
#define MIN -1000
#define MAX 1000

#include <iostream>
using namespace std;

struct NMK
{
    int N = 0;
    int M = 0;
    int K = 0;
};

struct Move
{
    int row, col;
};

void PrintBoard(NMK& Solver, int** board)
{
    for (int i = 0; i < Solver.N; i++)
    {
        for (int j = 0; j < Solver.M; j++)
        {
            printf("%i ", board[i][j]);
        }
        printf("\n");
    }
}

int CountPossibilities(NMK& Solver, int** board)
{
    int pos = 0;
    for (int i = 0; i < Solver.N; i++)
    {
        for (int j = 0; j < Solver.M; j++)
        {
            if (board[i][j] == 0)
            {
                pos++;
            }
        }
    }
    return pos;
}

void SetToFalse(NMK& Solver, bool** changed)
{
    for (int i = 0; i < Solver.N; i++)
    {
        for (int j = 0; j < Solver.M; j++)
        {
            changed[i][j] = false;
        }
    }
}

bool VerticalWin(NMK& Solver, int** tmp)
{
    int Kcounter = 0;
    for (int p = 1; p < 3; p++) //2 players
    {
        for (int i = 0; i < Solver.N; i++)
        {
            for (int j = 0; j < Solver.M; j++)
            {
                if (tmp[i][j] == p)
                {
                    Kcounter++;
                    int col = j;
                    for (int k = i + 1; k < Solver.N; k++) //field below
                    {
                        if (tmp[k][col] == p)
                        {
                            Kcounter++;
                            if (Kcounter == Solver.K)
                            {
                                return true;
                            }
                        }
                        else
                        {
                            Kcounter = 0;
                            break;
                        }
                    }
                }
                else
                {
                    Kcounter = 0;
                }
            }
        }
        Kcounter = 0;
    }
    return false;
}

bool HorizontalWin(NMK& Solver, int** tmp)
{
    int Kcounter = 0;
    for (int p = 1; p < 3; p++) //2 players
    {
        for (int i = 0; i < Solver.N; i++)
        {
            for (int j = 0; j < Solver.M; j++)
            {
                if (tmp[i][j] == p)
                {
                    Kcounter++;
                    int row = i;
                    for (int k = j + 1; k < Solver.M; k++) //field next to
                    {
                        if (tmp[row][k] == p)
                        {
                            Kcounter++;
                            if (Kcounter == Solver.K)
                            {
                                return true;
                            }
                        }
                        else
                        {
                            Kcounter = 0;
                            break;
                        }
                    }
                }
                else
                {
                    Kcounter = 0;
                }
            }
            Kcounter = 0;
        }
        Kcounter = 0;
    }
    return false;
}

bool DiagonalDownWin(NMK& Solver, int** tmp)
{
    int Kcounter = 0;
    int y, x = { 0 };
    for (int p = 1; p < 3; p++)
    {
        for (int i = 0; i < Solver.N; i++)
        {
            for (int j = 0; j < Solver.M; j++)
            {
                if (tmp[i][j] == p)
                {
                    Kcounter++;
                    y = i;
                    x = j;
                    while (y + 1 < Solver.N && x + 1 < Solver.M) //not out of board
                    {
                        if (tmp[y + 1][x + 1] == tmp[y][x])
                        {
                            Kcounter++;
                        }
                        else
                        {
                            Kcounter = 0;
                        }
                        if (Kcounter == Solver.K)
                        {
                            return true;
                        }
                        y++;
                        x++;
                    }
                }
                Kcounter = 0;
            }
        }
        Kcounter = 0;
    }
    return false;
}

bool DiagonalUpWin(NMK& Solver, int** tmp)
{
    int Kcounter = 0;
    int y, x = { 0 };
    for (int p = 1; p < 3; p++)
    {
        for (int i = Solver.N - 1; i >= 0; i--) //left bottom corner
        {
            for (int j = 0; j < Solver.M; j++)
            {
                if (tmp[i][j] == p)
                {
                    Kcounter++;
                    y = i;
                    x = j;
                    while (y - 1 >= 0 && x + 1 < Solver.M) //not out of board
                    {
                        if (tmp[y - 1][x + 1] == tmp[y][x])
                        {
                            Kcounter++;
                        }
                        else
                        {
                            Kcounter = 0;
                        }
                        if (Kcounter == Solver.K)
                        {
                            return true;
                        }
                        y--;
                        x++;
                    }
                }
                Kcounter = 0;
            }
        }
        Kcounter = 0;
    }
    return false;
}

int VerticalWin_SOLVE(NMK& Solver, int** tmp, int player, int opponent)
{
    int KcounterPlayer = 0;
    int KcounterOpp = 0;
    for (int i = 0; i < Solver.N; i++)
    {
        for (int j = 0; j < Solver.M; j++)
        {
            if (tmp[i][j] == player)
            {
                KcounterPlayer++;
                int col = j;
                for (int k = i + 1; k < Solver.N; k++) //field below
                {
                    if (tmp[k][col] == player)
                    {
                        KcounterPlayer++;
                        if (KcounterPlayer == Solver.K)
                        {
                            return 1;
                        }
                    }
                    else
                    {
                        KcounterPlayer = 0;
                        break;
                    }
                }
            }
            else if (tmp[i][j] == opponent)
            {
                KcounterOpp++;
                int col = j;
                for (int k = i + 1; k < Solver.N; k++) //field below
                {
                    if (tmp[k][col] == opponent)
                    {
                        KcounterOpp++;
                        if (KcounterOpp == Solver.K)
                        {
                            return -1;
                        }
                    }
                    else
                    {
                        KcounterOpp = 0;
                        break;
                    }
                }
            }
            else
            {
                KcounterPlayer = 0;
                KcounterOpp = 0;
            }
        }
    }
    KcounterPlayer = 0;
    KcounterOpp = 0;
    return 0;
}

int HorizontalWin_SOLVE(NMK& Solver, int** tmp, int player, int opponent)
{
    int KcounterPlayer = 0;
    int KcounterOpp = 0;
    for (int i = 0; i < Solver.N; i++)
    {
        for (int j = 0; j < Solver.M; j++)
        {
            if (tmp[i][j] == player)
            {
                KcounterPlayer++;
                int row = i;
                for (int k = j + 1; k < Solver.M; k++) //field next to
                {
                    if (tmp[row][k] == player)
                    {
                        KcounterPlayer++;
                        if (KcounterPlayer == Solver.K)
                        {
                            return 1;
                        }
                    }
                    else
                    {
                        KcounterPlayer = 0;
                        break;
                    }
                }
            }
            else if (tmp[i][j] == opponent)
            {
                KcounterOpp++;
                int row = i;
                for (int k = j + 1; k < Solver.M; k++) //field next to
                {
                    if (tmp[row][k] == opponent)
                    {
                        KcounterOpp++;
                        if (KcounterOpp == Solver.K)
                        {
                            return -1;
                        }
                    }
                    else
                    {
                        KcounterOpp = 0;
                        break;
                    }
                }
            }
            else
            {
                KcounterPlayer = 0;
                KcounterOpp = 0;
            }
        }
        KcounterPlayer = 0;
        KcounterOpp = 0;
    }
    KcounterPlayer = 0;
    KcounterOpp = 0;
    return 0;
}

int DiagonalDownWin_SOLVE(NMK& Solver, int** tmp, int player, int opponent)
{
    int KcounterPlayer = 0;
    int KcounterOpp = 0;
    int y, x = { 0 };
    for (int i = 0; i < Solver.N; i++)
    {
        for (int j = 0; j < Solver.M; j++)
        {
            if (tmp[i][j] == player)
            {
                KcounterPlayer++;
                y = i;
                x = j;
                while (y + 1 < Solver.N && x + 1 < Solver.M) //not out of board
                {
                    if (tmp[y + 1][x + 1] == tmp[y][x])
                    {
                        KcounterPlayer++;
                    }
                    else
                    {
                        KcounterPlayer = 0;
                    }
                    if (KcounterPlayer == Solver.K)
                    {
                        return 1;
                    }
                    y++;
                    x++;
                }
            }
            else if (tmp[i][j] == opponent)
            {
                KcounterOpp++;
                y = i;
                x = j;
                while (y + 1 < Solver.N && x + 1 < Solver.M) //not out of board
                {
                    if (tmp[y + 1][x + 1] == tmp[y][x])
                    {
                        KcounterOpp++;
                    }
                    else
                    {
                        KcounterOpp = 0;
                    }
                    if (KcounterOpp == Solver.K)
                    {
                        return -1;
                    }
                    y++;
                    x++;
                }
            }
            KcounterPlayer = 0;
            KcounterOpp = 0;
        }
    }
    KcounterPlayer = 0;
    KcounterOpp = 0;
    return 0;
}

int DiagonalUpWin_SOLVE(NMK& Solver, int** tmp, int player, int opponent)
{
    int KcounterPlayer = 0;
    int KcounterOpp = 0;
    int y, x = { 0 };
    for (int i = Solver.N - 1; i >= 0; i--) //left bottom corner
    {
        for (int j = 0; j < Solver.M; j++)
        {
            if (tmp[i][j] == player)
            {
                KcounterPlayer++;
                y = i;
                x = j;
                while (y - 1 >= 0 && x + 1 < Solver.M) //not out of board
                {
                    if (tmp[y - 1][x + 1] == tmp[y][x])
                    {
                        KcounterPlayer++;
                    }
                    else
                    {
                        KcounterPlayer = 0;
                    }
                    if (KcounterPlayer == Solver.K)
                    {
                        return 1;
                    }
                    y--;
                    x++;
                }
            }
            else if (tmp[i][j] == opponent)
            {
                KcounterOpp++;
                y = i;
                x = j;
                while (y - 1 >= 0 && x + 1 < Solver.M) //not out of board
                {
                    if (tmp[y - 1][x + 1] == tmp[y][x])
                    {
                        KcounterOpp++;
                    }
                    else
                    {
                        KcounterOpp = 0;
                    }
                    if (KcounterOpp == Solver.K)
                    {
                        return -1;
                    }
                    y--;
                    x++;
                }
            }
            KcounterPlayer = 0;
            KcounterOpp = 0;
        }
    }
    KcounterPlayer = 0;
    KcounterOpp = 0;
    return 0;
}

void FreeMemory(NMK& Solver, int** board)
{
    for (int i = 0; i < Solver.N; i++)
    {
        delete[] board[i];
    }
    delete[] board;
}

bool AlreadyWin(NMK& Solver, int** board)
{
    if (VerticalWin(Solver, board))
    {
        return true;
    }
    if (HorizontalWin(Solver, board))
    {
        return true;
    }
    if (DiagonalDownWin(Solver, board))
    {
        return true;
    }
    if (DiagonalUpWin(Solver, board))
    {
        return true;
    }
    return false;
}

void PrintPossibilities(NMK& Solver, int** board, int player, int countP, bool** changed)
{
    bool modified = false;
    printf("%i \n", countP);
    for (int h = 0; h < countP; h++)
    {
        for (int i = 0; i < Solver.N; i++)
        {
            for (int j = 0; j < Solver.M; j++)
            {
                if (board[i][j] == 0 && changed[i][j] == false && modified == false)
                {
                    printf("%i ", player);
                    changed[i][j] = true;
                    modified = true;
                }
                else
                {
                    printf("%i ", board[i][j]);
                }
            }
            printf("\n");
        }
        modified = false;
    }
}

int AlreadyWin_SOLVE(NMK& Solver, int** board, int player, int opponent)
{
    if (VerticalWin_SOLVE(Solver, board, player, opponent) != 0)
    {
        return VerticalWin_SOLVE(Solver, board, player, opponent);
    }
    else if (HorizontalWin_SOLVE(Solver, board, player, opponent) != 0)
    {
        return HorizontalWin_SOLVE(Solver, board, player, opponent);
    }
    else if (DiagonalDownWin_SOLVE(Solver, board, player, opponent) != 0)
    {
        return DiagonalDownWin_SOLVE(Solver, board, player, opponent);
    }
    else if (DiagonalUpWin_SOLVE(Solver, board, player, opponent) != 0)
    {
        return DiagonalUpWin_SOLVE(Solver, board, player, opponent);
    }
    else
    {
        return 0;
    }
}

bool CheckWin(NMK& Solver, int** board, int player, int countP, bool** changed)
{
    bool modified = false;
    int col = 0;
    int row = 0;
    for (int h = 0; h < countP; h++)
    {
        for (int i = 0; i < Solver.N; i++)
        {
            for (int j = 0; j < Solver.M; j++)
            {
                if (board[i][j] == 0 && changed[i][j] == false && modified == false)
                {
                    col = j;
                    row = i;
                    board[i][j] = player;
                    changed[i][j] = true;
                    modified = true;
                }
            }
        }
        if (AlreadyWin(Solver, board))
        {
            printf("1 \n");
            PrintBoard(Solver, board);
            return true;
        }
        modified = false;
        board[row][col] = 0;
    }
    return false;
}

void FreeTmp(NMK& Solver, bool** changed)
{
    for (int i = 0; i < Solver.N; i++)
    {
        delete[] changed[i];
    }
    delete[] changed;
}

void Possibilities(NMK& Solver, int** board, int player, int countP, const int option)
{
    bool** changed = new bool* [Solver.N];
    for (int i = 0; i < Solver.N; i++) //2d dynamic array
    {
        changed[i] = new bool[Solver.M];
    }
    SetToFalse(Solver, changed);
    bool win = false;

    if (AlreadyWin(Solver, board))
    {
        printf("0 \n");
        win = 1;
    }

    else if (!win)
    {
        if (option == ifgo)
        {
            if (CheckWin(Solver, board, player, countP, changed))
            {
                return;
            }
        }
        SetToFalse(Solver, changed);
        PrintPossibilities(Solver, board, player, countP, changed);
    }
    FreeTmp(Solver, changed);
}

void CreateBoard(NMK& Solver, int** board)
{
    for (int i = 0; i < Solver.N; i++) //2d dynamic array
    {
        board[i] = new int[Solver.M];
        for (int j = 0; j < Solver.M; j++) //enter board
        {
            scanf("%i", &board[i][j]);
        }
    }
}

int getOpponent(int player)
{
    int opponent = 0;
    if (player == 1)
    {
        opponent = 2;
        return opponent;
    }
    else if (player == 2)
    {
        opponent = 1;
        return opponent;
    }
    return opponent;
}

bool isMovesLeft(NMK& Solver, int** board)
{
    for (int i = 0; i < Solver.N; i++)
        for (int j = 0; j < Solver.M; j++)
            if (board[i][j] == 0)
                return true;
    return false;
}

int minimax(NMK& Solver, int** board, int player, int opponent, bool isMax, int alpha, int beta)
{
    int score = AlreadyWin_SOLVE(Solver, board, player, opponent);

    // If Maximizer has won the game return his/her
    // evaluated score
    if (score == 1)
        return score;

    // If Minimizer has won the game return his/her
    // evaluated score
    if (score == -1)
        return score;

    // If there are no more moves and no winner then
    // it is a tie
    if (isMovesLeft(Solver, board) == false)
        return 0;

    // If this maximizer's move
    if (isMax)
    {
        int best = -1000;

        // Traverse all cells
        for (int i = 0; i < Solver.N; i++)
        {
            for (int j = 0; j < Solver.M; j++)
            {
                // Check if cell is empty
                if (board[i][j] == 0)
                {
                    // Make the move
                    board[i][j] = player;

                    // Call minimax recursively and choose
                    // the maximum value
                    int mim = minimax(Solver, board, player, opponent, !isMax, alpha, beta);
                    if (mim > best)
                    {
                        best = mim;
                    }
                    // Undo the move
                    board[i][j] = 0;
                    if (best > alpha)
                    {
                        alpha = best;
                    }
                    // Alpha Beta Pruning
                    if (beta <= alpha)
                        break;
                }
            }
        }
        return best;
    }

    // If this minimizer's move
    else
    {
        int best = 1000;

        // Traverse all cells
        for (int i = 0; i < Solver.N; i++)
        {
            for (int j = 0; j < Solver.M; j++)
            {
                // Check if cell is empty
                if (board[i][j] == 0)
                {
                    // Make the move
                    board[i][j] = opponent;

                    // Call minimax recursively and choose
                    // the minimum value
                    int mim = minimax(Solver, board, player, opponent, !isMax, alpha, beta);
                    if (mim < best)
                    {
                        best = mim;
                    }
                    // Undo the move
                    board[i][j] = 0;

                    if (best < beta)
                    {
                        beta = best;
                    }

                    // Alpha Beta Pruning
                    if (beta <= alpha)
                        break;
                }
            }
        }
        return best;
    }
}

Move findBestMove(NMK& Solver, int** board, int player, int opponent)
{
    int bestVal = -1000;
    Move bestMove;
    bestMove.row = -1;
    bestMove.col = -1;

    // Traverse all cells, evaluate minimax function for
    // all empty cells. And return the cell with optimal
    // value.
    for (int i = 0; i < Solver.N; i++)
    {
        for (int j = 0; j < Solver.M; j++)
        {
            // Check if cell is empty
            if (board[i][j] == 0)
            {
                // Make the move
                board[i][j] = player;

                // compute evaluation function for this
                // move.
                int moveVal = minimax(Solver, board, player, opponent, false, MIN, MAX);

                // Undo the move
                board[i][j] = 0;

                // If the value of the current move is
                // more than the best value, then update
                // best/
                if (moveVal > bestVal)
                {
                    bestMove.row = i;
                    bestMove.col = j;
                    bestVal = moveVal;
                }
            }
        }
    }
    return bestMove;
}

void SolveGameState(NMK& Solver, int** board, int player)
{
    for (;;)
    {
        int opponent = getOpponent(player);
        int GameOver = AlreadyWin_SOLVE(Solver, board, player, opponent);
        if (GameOver == 1)//player wins
        {
            if (player == 1)
            {
                printf("FIRST_PLAYER_WINS\n");
                return;
            }
            else if (player == 2)
            {
                printf("SECOND_PLAYER_WINS\n");
                return;
            }
        }
        else if (GameOver == -1)//opponent wins
        {
            if (player == 1)
            {
                printf("SECOND_PLAYER_WINS\n");
                return;
            }
            else if (player == 2)
            {
                printf("FIRST_PLAYER_WINS\n");
                return;
            }
        }
        else
        {
            if (isMovesLeft(Solver, board) == false)
            {
                printf("BOTH_PLAYERS_TIE\n");
                return;
            }
        }
        Move bestmove = findBestMove(Solver, board, player, opponent);
        board[bestmove.row][bestmove.col] = player;
        player = opponent;
    }
}

int main()
{
    char cmd[buffor] = "";
    NMK Solver;
    int player = 0;
    int countP = 0;
    const int firstcmd = basic; //"gen all pos mov" command
    const int secondcmd = ifgo; //"if game over" command 
    while (true)
    {
        scanf("%50s", &cmd);
        if (feof(stdin) != 0)
        {
            return 0;
        }
        else if ((strcmp(cmd, "GEN_ALL_POS_MOV") == 0))
        {
            scanf("%i %i %i %i", &Solver.N, &Solver.M, &Solver.K, &player);
            int** board = new int* [Solver.N];
            CreateBoard(Solver, board);
            countP = CountPossibilities(Solver, board);
            Possibilities(Solver, board, player, countP, firstcmd);
            FreeMemory(Solver, board);
        }
        else if ((strcmp(cmd, "GEN_ALL_POS_MOV_CUT_IF_GAME_OVER") == 0))
        {
            scanf("%i %i %i %i", &Solver.N, &Solver.M, &Solver.K, &player);
            int** board = new int* [Solver.N];
            CreateBoard(Solver, board);
            countP = CountPossibilities(Solver, board);
            Possibilities(Solver, board, player, countP, secondcmd);
            FreeMemory(Solver, board);
        }
        else if ((strcmp(cmd, "SOLVE_GAME_STATE") == 0))
        {
            scanf("%i %i %i %i", &Solver.N, &Solver.M, &Solver.K, &player);
            int** board = new int* [Solver.N];
            CreateBoard(Solver, board);
            SolveGameState(Solver, board, player);
            FreeMemory(Solver, board);
        }
    }
    return 0;
}