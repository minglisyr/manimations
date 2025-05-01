from manim import *

class FluidFlow(Scene):
    def construct(self):
        # Define vector field (e.g., sinusoidal flow)
        func = lambda pos: np.sin(pos[0]/2) * UR + np.cos(pos[1]/2) * LEFT
        
        # Configure streamlines
        stream_lines = StreamLines(
            func,
            stroke_width=3,
            max_anchors_per_line=30,
            virtual_time=1,
            color=RED
        )
        
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(5)
