import turtle
import random

# Define the draw_spiral function that takes length, angle, and pattern as inputs
def draw_spiral(length, angle, pattern):
    # List of colors for the spiral
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    # Loop through the range of the given length
    for i in range(length):
        # If pattern is 1, set the turtle color randomly from the list of colors
        if pattern == 1:
            my_turtle.color(random.choice(colors))
        # If pattern is 2, cycle through the list of colors
        elif pattern == 2:
            my_turtle.color(colors[i % len(colors)])

        # Move the turtle forward by the current value of i and rotate by the given angle
        my_turtle.forward(i)
        my_turtle.right(angle)

# Main function
if __name__ == '__main__':
    # Set up the turtle screen with a black background and a title
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Colorful Spiral")

    # Set up the turtle with zero speed
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)

    # Get user input for the length, angle, and pattern of the spiral
    length = int(input("Enter the length of the spiral (e.g., 100): "))
    angle = int(input("Enter the angle for the spiral (e.g., 91): "))
    pattern = int(input("Choose a color pattern (1: random colors, 2: cycle through colors): "))

    # Draw a colorful spiral with the given parameters
    draw_spiral(length, angle, pattern)

    # Ask the user if they want to save the output as an image
    save_choice = input("Do you want to save the output as an image? (y/n): ")
    # If the user chooses 'y', save the output as an EPS image
    if save_choice.lower() == 'y':
        canvas = turtle.getcanvas()
        canvas.postscript(file="spiral_output.eps", colormode='color')

    # Keep the window open until it's manually closed
    turtle.done()