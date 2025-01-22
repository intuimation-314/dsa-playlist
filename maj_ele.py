from manim import *

class MajorityElement(Scene):
    def create_pointer(self, position, label_text):
        """Creates a pointer with a label below the given position."""
        pointer = Triangle(fill_opacity=1, color=RED).scale(0.2)
        pointer.next_to(position, DOWN)
        label = Text(label_text, font_size=24).next_to(pointer, DOWN * 0.2)
        return VGroup(pointer, label)

    def display_code(self, code_text):
        """Displays the C++ code at the bottom."""
        code = Code(
            code=code_text,
            tab_width=4,
            background="window",
            language="C++",
            font_size=18,
            insert_line_no=False,
            line_spacing=0.6
        ).move_to(2* DOWN).scale(0.8)
        self.play(Create(code))
        return code

    def construct(self):
        # Title Text
        title = Text("Majority Element Algorithm", gradient=[BLUE, PURPLE]).move_to(3 * UP).scale(1.2)
        self.add(title)

        # Code snippet
        cpp_code = """
int majorityElement(vector<int>& nums) {
    int freq = 1, maj_el = nums[0], n = nums.size();
    sort(nums.begin(), nums.end());
    for (int i = 1; i < n; i++) {
        if (nums[i] == nums[i - 1]) freq++;
        else freq = 1, maj_el = nums[i];
        if (freq > n / 2) return nums[i];
    }
    return maj_el;
}
        """
        code_display = self.display_code(cpp_code)

        # Initial unsorted array
        nums = [3, 3, 4, 2, 4, 4, 2, 4, 4, 3, 3, 3, 4, 4, 4]
        array = VGroup(*[Square().scale(0.4) for _ in nums]).arrange(RIGHT, buff=0.1).move_to(1.5 * UP)
        num_tex = VGroup(*[MathTex(str(num)) for num in nums]).scale(1.5).arrange(RIGHT).scale(0.75)
        [num_tex[i].move_to(array[i].get_center()) for i in range(len(nums))]
        self.play(Create(array), Create(num_tex))

        # Sort the array visually
        self.wait(1)
        nums.sort()  # Sort the array
        sorted_tex = VGroup(*[MathTex(str(num)) for num in nums]).scale(1.5).arrange(RIGHT).scale(0.8)
        [sorted_tex[i].move_to(array[i].get_center()) for i in range(len(nums))]
        self.play(Transform(num_tex, sorted_tex))
        self.wait(1)

        # Initial variable values
        freq_text = Tex("freq =", "1").to_edge(LEFT)
        maj_el_text = Tex("maj\\_el =", f"{nums[0]}").to_edge(LEFT).shift(0.5 * DOWN)
        self.play(Write(freq_text), Write(maj_el_text))

        n = len(nums)
        freq = 1
        maj_el = nums[0]

        # Algorithm visualization
        i_pointer = self.create_pointer(num_tex[0].get_center(), "i")
        self.play(Create(i_pointer))

        for i in range(1, n):
            # Move pointer to the next position
            self.play(i_pointer.animate.next_to(num_tex[i].get_center(), DOWN))

            # Update frequency or reset it
            if nums[i] == nums[i - 1]:
                freq += 1
            else:
                freq = 1
                maj_el = nums[i]

            # Update variable displays
            new_freq_text = Tex(f"{freq}").move_to(freq_text[1].get_center())
            new_maj_el_text = Tex(f"{maj_el}").move_to(maj_el_text[1].get_center())
            self.play(Transform(freq_text[1], new_freq_text), Transform(maj_el_text[1], new_maj_el_text))

            # Highlight the majority element candidate
            self.play(num_tex[i].animate.set_color(YELLOW))
            self.wait(0.5)
            self.play(num_tex[i].animate.set_color(WHITE))

            # Check for majority element
            if freq > n / 2:
                self.play(Indicate(num_tex[i], color=GREEN))
                break

        # Final wait before ending the scene
        self.play(FadeOut(code_display), FadeOut(freq_text), FadeOut(maj_el_text), FadeOut(i_pointer))
        self.wait(1)
