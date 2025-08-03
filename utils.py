# import random

# SOLVED_STATE = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
# MOVES = ["U", "U'", "D", "D'", "L", "L'", "R", "R'", "F", "F'", "B", "B'"]

# def generate_valid_scramble(num_moves=25):
#     current_state = SOLVED_STATE
#     for _ in range(num_moves):
#         move = random.choice(MOVES)
#         current_state = apply_move(current_state, move)
#     return current_state

# def get_cube_state():
#     while True:
#         scramble = generate_valid_scramble()
#         if scramble != SOLVED_STATE:
#             return scramble

# def rotate_face(state, face_start, clockwise=True):
#     positions = list(range(face_start, face_start + 9))
#     original = [state[p] for p in positions]
#     if clockwise:
#         rotated = [original[6], original[3], original[0], original[7], original[4], original[1], original[8], original[5], original[2]]
#     else:
#         rotated = [original[2], original[5], original[8], original[1], original[4], original[7], original[0], original[3], original[6]]
#     for i, p in enumerate(positions):
#         state[p] = rotated[i]

# def apply_move(cube_state, move):
#     state = list(cube_state)
#     if move == 'U':
#         rotate_face(state, 0, True)
#         temp = [state[45], state[46], state[47]]
#         state[45:48] = state[9:12]
#         state[9:12] = state[18:21]
#         state[18:21] = state[36:39]
#         state[36:39] = temp
#     elif move == "U'":
#         rotate_face(state, 0, False)
#         temp = [state[36], state[37], state[38]]
#         state[36:39] = state[18:21]
#         state[18:21] = state[9:12]
#         state[9:12] = state[45:48]
#         state[45:48] = temp
#     # Add similar blocks for D, F, B, L, R (expand as needed for full accuracy)
#     return ''.join(state)

# def predict_states(scramble, solution):
#     if "Error" in solution:
#         return ["Cannot predict - invalid scramble"]
#     states = [scramble]
#     current = scramble
#     moves = solution.split()
#     for move in moves:
#         current = apply_move(current, move)
#         states.append(current)
#     return states if states[-1] == SOLVED_STATE else ["Prediction error - check move cycles"]

# if __name__ == "__main__":
#     print("Testing utils.py")
#     print(get_cube_state())

# import random

# SOLVED_STATE = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
# MOVES = ["U", "U'", "D", "D'", "L", "L'", "R", "R'", "F", "F'", "B", "B'"]

# def generate_valid_scramble(num_moves=25):
#     current_state = SOLVED_STATE
#     for _ in range(num_moves):
#         move = random.choice(MOVES)
#         current_state = apply_move(current_state, move)
#     return current_state

# def get_cube_state():
#     while True:
#         scramble = generate_valid_scramble()
#         if scramble != SOLVED_STATE:
#             return scramble

# def rotate_face(state, face_start, clockwise=True):
#     positions = list(range(face_start, face_start + 9))
#     original = [state[p] for p in positions]
#     if clockwise:
#         rotated = [original[6], original[3], original[0], original[7], original[4], original[1], original[8], original[5], original[2]]
#     else:
#         rotated = [original[2], original[5], original[8], original[1], original[4], original[7], original[0], original[3], original[6]]
#     for i, p in enumerate(positions):
#         state[p] = rotated[i]

# def apply_move(cube_state, move):
#     state = list(cube_state)
    
#     # Define face start indices for each face
#     U_START, R_START, F_START, D_START, L_START, B_START = 0, 9, 18, 27, 36, 45
    
#     if move == 'U':
#         rotate_face(state, U_START, True)
#         temp = [state[R_START + 0], state[R_START + 1], state[R_START + 2]]
#         state[R_START + 0:R_START + 3] = state[F_START + 0:F_START + 3]
#         state[F_START + 0:F_START + 3] = state[L_START + 0:L_START + 3]
#         state[L_START + 0:L_START + 3] = state[B_START + 0:B_START + 3]
#         state[B_START + 0:B_START + 3] = temp
#     elif move == "U'":
#         rotate_face(state, U_START, False)
#         temp = [state[R_START + 0], state[R_START + 1], state[R_START + 2]]
#         state[R_START + 0:R_START + 3] = state[B_START + 0:B_START + 3]
#         state[B_START + 0:B_START + 3] = state[L_START + 0:L_START + 3]
#         state[L_START + 0:L_START + 3] = state[F_START + 0:F_START + 3]
#         state[F_START + 0:F_START + 3] = temp

#     elif move == 'D':
#         rotate_face(state, D_START, True)
#         temp = [state[R_START + 6], state[R_START + 7], state[R_START + 8]]
#         state[R_START + 6:R_START + 9] = state[B_START + 6:B_START + 9]
#         state[B_START + 6:B_START + 9] = state[L_START + 6:L_START + 9]
#         state[L_START + 6:L_START + 9] = state[F_START + 6:F_START + 9]
#         state[F_START + 6:F_START + 9] = temp
#     elif move == "D'":
#         rotate_face(state, D_START, False)
#         temp = [state[R_START + 6], state[R_START + 7], state[R_START + 8]]
#         state[R_START + 6:R_START + 9] = state[F_START + 6:F_START + 9]
#         state[F_START + 6:F_START + 9] = state[L_START + 6:L_START + 9]
#         state[L_START + 6:L_START + 9] = state[B_START + 6:B_START + 9]
#         state[B_START + 6:B_START + 9] = temp

#     elif move == 'F':
#         rotate_face(state, F_START, True)
#         temp = [state[U_START + 6], state[U_START + 7], state[U_START + 8]]
#         state[U_START + 6], state[U_START + 7], state[U_START + 8] = state[L_START + 8], state[L_START + 5], state[L_START + 2]
#         state[L_START + 2], state[L_START + 5], state[L_START + 8] = state[D_START + 0], state[D_START + 1], state[D_START + 2]
#         state[D_START + 0], state[D_START + 1], state[D_START + 2] = state[R_START + 6], state[R_START + 3], state[R_START + 0]
#         state[R_START + 0], state[R_START + 3], state[R_START + 6] = temp[0], temp[1], temp[2]
#     elif move == "F'":
#         rotate_face(state, F_START, False)
#         temp = [state[U_START + 6], state[U_START + 7], state[U_START + 8]]
#         state[U_START + 6], state[U_START + 7], state[U_START + 8] = state[R_START + 0], state[R_START + 3], state[R_START + 6]
#         state[R_START + 0], state[R_START + 3], state[R_START + 6] = state[D_START + 2], state[D_START + 1], state[D_START + 0]
#         state[D_START + 0], state[D_START + 1], state[D_START + 2] = state[L_START + 2], state[L_START + 5], state[L_START + 8]
#         state[L_START + 2], state[L_START + 5], state[L_START + 8] = temp[2], temp[1], temp[0]

#     elif move == 'B':
#         rotate_face(state, B_START, True)
#         temp = [state[U_START + 0], state[U_START + 1], state[U_START + 2]]
#         state[U_START + 0], state[U_START + 1], state[U_START + 2] = state[R_START + 2], state[R_START + 5], state[R_START + 8]
#         state[R_START + 2], state[R_START + 5], state[R_START + 8] = state[D_START + 8], state[D_START + 7], state[D_START + 6]
#         state[D_START + 6], state[D_START + 7], state[D_START + 8] = state[L_START + 6], state[L_START + 3], state[L_START + 0]
#         state[L_START + 0], state[L_START + 3], state[L_START + 6] = temp[0], temp[1], temp[2]
#     elif move == "B'":
#         rotate_face(state, B_START, False)
#         temp = [state[U_START + 0], state[U_START + 1], state[U_START + 2]]
#         state[U_START + 0], state[U_START + 1], state[U_START + 2] = state[L_START + 0], state[L_START + 3], state[L_START + 6]
#         state[L_START + 0], state[L_START + 3], state[L_START + 6] = state[D_START + 6], state[D_START + 7], state[D_START + 8]
#         state[D_START + 6], state[D_START + 7], state[D_START + 8] = state[R_START + 8], state[R_START + 5], state[R_START + 2]
#         state[R_START + 2], state[R_START + 5], state[R_START + 8] = temp[0], temp[1], temp[2]

#     elif move == 'L':
#         rotate_face(state, L_START, True)
#         temp = [state[U_START + 0], state[U_START + 3], state[U_START + 6]]
#         state[U_START + 0], state[U_START + 3], state[U_START + 6] = state[B_START + 8], state[B_START + 5], state[B_START + 2]
#         state[B_START + 2], state[B_START + 5], state[B_START + 8] = state[D_START + 0], state[D_START + 3], state[D_START + 6]
#         state[D_START + 0], state[D_START + 3], state[D_START + 6] = state[F_START + 0], state[F_START + 3], state[F_START + 6]
#         state[F_START + 0], state[F_START + 3], state[F_START + 6] = temp[0], temp[1], temp[2]
#     elif move == "L'":
#         rotate_face(state, L_START, False)
#         temp = [state[U_START + 0], state[U_START + 3], state[U_START + 6]]
#         state[U_START + 0], state[U_START + 3], state[U_START + 6] = state[F_START + 0], state[F_START + 3], state[F_START + 6]
#         state[F_START + 0], state[F_START + 3], state[F_START + 6] = state[D_START + 0], state[D_START + 3], state[D_START + 6]
#         state[D_START + 0], state[D_START + 3], state[D_START + 6] = state[B_START + 8], state[B_START + 5], state[B_START + 2]
#         state[B_START + 2], state[B_START + 5], state[B_START + 8] = temp[0], temp[1], temp[2]
        
#     elif move == 'R':
#         rotate_face(state, R_START, True)
#         temp = [state[U_START + 2], state[U_START + 5], state[U_START + 8]]
#         state[U_START + 2], state[U_START + 5], state[U_START + 8] = state[F_START + 2], state[F_START + 5], state[F_START + 8]
#         state[F_START + 2], state[F_START + 5], state[F_START + 8] = state[D_START + 2], state[D_START + 5], state[D_START + 8]
#         state[D_START + 2], state[D_START + 5], state[D_START + 8] = state[B_START + 6], state[B_START + 3], state[B_START + 0]
#         state[B_START + 0], state[B_START + 3], state[B_START + 6] = temp[2], temp[1], temp[0]
#     elif move == "R'":
#         rotate_face(state, R_START, False)
#         temp = [state[U_START + 2], state[U_START + 5], state[U_START + 8]]
#         state[U_START + 2], state[U_START + 5], state[U_START + 8] = state[B_START + 6], state[B_START + 3], state[B_START + 0]
#         state[B_START + 0], state[B_START + 3], state[B_START + 6] = state[D_START + 8], state[D_START + 5], state[D_START + 2]
#         state[D_START + 2], state[D_START + 5], state[D_START + 8] = state[F_START + 2], state[F_START + 5], state[F_START + 8]
#         state[F_START + 2], state[F_START + 5], state[F_START + 8] = temp[0], temp[1], temp[2]
        
#     return ''.join(state)

# def predict_states(scramble, solution):
#     if "Error" in solution:
#         return ["Cannot predict - invalid scramble"]
#     states = [scramble]
#     current = scramble
#     moves = solution.split()
#     for move in moves:
#         current = apply_move(current, move)
#         states.append(current)
#     return states if states[-1] == SOLVED_STATE else ["Prediction error - check move cycles"]

# if __name__ == "__main__":
#     print("Testing utils.py")
#     print(get_cube_state())

import random

SOLVED_STATE = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
MOVES = ["U", "U'", "D", "D'", "L", "L'", "R", "R'", "F", "F'", "B", "B'"]

def generate_valid_scramble(num_moves=25):
    """Generates a valid scrambled state by applying random moves to a solved cube."""
    current_state = SOLVED_STATE
    for _ in range(num_moves):
        move = random.choice(MOVES)
        current_state = apply_move(current_state, move)
    return current_state

def get_cube_state():
    """Returns a non-solved, randomly scrambled cube state."""
    while True:
        scramble = generate_valid_scramble()
        if scramble != SOLVED_STATE:
            return scramble

def rotate_face(state, face_start, clockwise=True):
    """Rotates a single face of the cube."""
    positions = list(range(face_start, face_start + 9))
    original = [state[p] for p in positions]
    if clockwise:
        rotated = [original[6], original[3], original[0], original[7], original[4], original[1], original[8], original[5], original[2]]
    else:
        rotated = [original[2], original[5], original[8], original[1], original[4], original[7], original[0], original[3], original[6]]
    for i, p in enumerate(positions):
        state[p] = rotated[i]

def apply_move(cube_state, move):
    """Applies a single move to the cube state and returns the new state."""
    state = list(cube_state)
    
    # Define face start indices for each face
    U, R, F, D, L, B = 0, 9, 18, 27, 36, 45
    
    if move == 'U':
        rotate_face(state, U, True)
        temp = state[F:F + 3]
        state[F:F + 3] = state[R:R + 3]
        state[R:R + 3] = state[B:B + 3]
        state[B:B + 3] = state[L:L + 3]
        state[L:L + 3] = temp
    elif move == "U'":
        rotate_face(state, U, False)
        temp = state[F:F + 3]
        state[F:F + 3] = state[L:L + 3]
        state[L:L + 3] = state[B:B + 3]
        state[B:B + 3] = state[R:R + 3]
        state[R:R + 3] = temp

    elif move == 'D':
        rotate_face(state, D, True)
        temp = state[F + 6:F + 9]
        state[F + 6:F + 9] = state[L + 6:L + 9]
        state[L + 6:L + 9] = state[B + 6:B + 9]
        state[B + 6:B + 9] = state[R + 6:R + 9]
        state[R + 6:R + 9] = temp
    elif move == "D'":
        rotate_face(state, D, False)
        temp = state[F + 6:F + 9]
        state[F + 6:F + 9] = state[R + 6:R + 9]
        state[R + 6:R + 9] = state[B + 6:B + 9]
        state[B + 6:B + 9] = state[L + 6:L + 9]
        state[L + 6:L + 9] = temp
        
    elif move == 'F':
        rotate_face(state, F, True)
        temp_U = [state[U + 6], state[U + 7], state[U + 8]]
        state[U + 6], state[U + 7], state[U + 8] = state[L + 8], state[L + 5], state[L + 2]
        state[L + 8], state[L + 5], state[L + 2] = state[D + 2], state[D + 1], state[D + 0]
        state[D + 2], state[D + 1], state[D + 0] = state[R + 0], state[R + 3], state[R + 6]
        state[R + 0], state[R + 3], state[R + 6] = temp_U[0], temp_U[1], temp_U[2]
    elif move == "F'":
        rotate_face(state, F, False)
        temp_U = [state[U + 6], state[U + 7], state[U + 8]]
        state[U + 6], state[U + 7], state[U + 8] = state[R + 0], state[R + 3], state[R + 6]
        state[R + 0], state[R + 3], state[R + 6] = state[D + 2], state[D + 1], state[D + 0]
        state[D + 2], state[D + 1], state[D + 0] = state[L + 8], state[L + 5], state[L + 2]
        state[L + 8], state[L + 5], state[L + 2] = temp_U[0], temp_U[1], temp_U[2]

    elif move == 'B':
        rotate_face(state, B, True)
        temp_U = [state[U + 0], state[U + 1], state[U + 2]]
        state[U + 0], state[U + 1], state[U + 2] = state[R + 2], state[R + 5], state[R + 8]
        state[R + 2], state[R + 5], state[R + 8] = state[D + 8], state[D + 7], state[D + 6]
        state[D + 8], state[D + 7], state[D + 6] = state[L + 6], state[L + 3], state[L + 0]
        state[L + 6], state[L + 3], state[L + 0] = temp_U[0], temp_U[1], temp_U[2]
    elif move == "B'":
        rotate_face(state, B, False)
        temp_U = [state[U + 0], state[U + 1], state[U + 2]]
        state[U + 0], state[U + 1], state[U + 2] = state[L + 6], state[L + 3], state[L + 0]
        state[L + 6], state[L + 3], state[L + 0] = state[D + 8], state[D + 7], state[D + 6]
        state[D + 8], state[D + 7], state[D + 6] = state[R + 2], state[R + 5], state[R + 8]
        state[R + 2], state[R + 5], state[R + 8] = temp_U[0], temp_U[1], temp_U[2]

    elif move == 'L':
        rotate_face(state, L, True)
        temp_U = [state[U + 0], state[U + 3], state[U + 6]]
        state[U + 0], state[U + 3], state[U + 6] = state[B + 8], state[B + 5], state[B + 2]
        state[B + 8], state[B + 5], state[B + 2] = state[D + 0], state[D + 3], state[D + 6]
        state[D + 0], state[D + 3], state[D + 6] = state[F + 0], state[F + 3], state[F + 6]
        state[F + 0], state[F + 3], state[F + 6] = temp_U[0], temp_U[1], temp_U[2]
    elif move == "L'":
        rotate_face(state, L, False)
        temp_U = [state[U + 0], state[U + 3], state[U + 6]]
        state[U + 0], state[U + 3], state[U + 6] = state[F + 0], state[F + 3], state[F + 6]
        state[F + 0], state[F + 3], state[F + 6] = state[D + 0], state[D + 3], state[D + 6]
        state[D + 0], state[D + 3], state[D + 6] = state[B + 8], state[B + 5], state[B + 2]
        state[B + 8], state[B + 5], state[B + 2] = temp_U[0], temp_U[1], temp_U[2]

    elif move == 'R':
        rotate_face(state, R, True)
        temp_U = [state[U + 2], state[U + 5], state[U + 8]]
        state[U + 2], state[U + 5], state[U + 8] = state[F + 2], state[F + 5], state[F + 8]
        state[F + 2], state[F + 5], state[F + 8] = state[D + 2], state[D + 5], state[D + 8]
        state[D + 2], state[D + 5], state[D + 8] = state[B + 6], state[B + 3], state[B + 0]
        state[B + 6], state[B + 3], state[B + 0] = temp_U[0], temp_U[1], temp_U[2]
    elif move == "R'":
        rotate_face(state, R, False)
        temp_U = [state[U + 2], state[U + 5], state[U + 8]]
        state[U + 2], state[U + 5], state[U + 8] = state[B + 6], state[B + 3], state[B + 0]
        state[B + 6], state[B + 3], state[B + 0] = state[D + 2], state[D + 5], state[D + 8]
        state[D + 2], state[D + 5], state[D + 8] = state[F + 2], state[F + 5], state[F + 8]
        state[F + 2], state[F + 5], state[F + 8] = temp_U[0], temp_U[1], temp_U[2]
        
    return ''.join(state)

def predict_states(scramble, solution):
    """Predicts all intermediate states from a scramble and solution."""
    if "Error" in solution or "No solution" in solution:
        return ["Prediction error - check move cycles"]
    states = [scramble]
    current = scramble
    moves = solution.split()
    for move in moves:
        try:
            current = apply_move(current, move)
            states.append(current)
        except IndexError as e:
            # Catching potential index errors in apply_move
            return [f"Prediction error - invalid move or state change. Details: {e}"]
    
    # Final check to see if the last state is the solved state.
    return states if states[-1] == SOLVED_STATE else ["Prediction error - check move cycles"]

if __name__ == "__main__":
    print("Testing utils.py")
    print(get_cube_state())
