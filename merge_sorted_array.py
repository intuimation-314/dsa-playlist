from manim import *

class MergeSortedArray(Scene):
    def create_pointer(self, position, label_text):
        """Creates a pointer with a label below the given position."""
        pointer = Triangle(fill_opacity=1, color=RED).scale(0.15)
        pointer.next_to(position, DOWN)
        label = Text(label_text, font_size=22).next_to(pointer, DOWN * 0.2)
        return VGroup(pointer, label)

    def display_code(self, code_text):
        """Displays code snippet at the bottom."""
        code = Code(
            code=code_text,
            tab_width=4,
            background="window",
            language="C++",
            font_size=18,
            insert_line_no=False,
            line_spacing=0.6
        ).move_to(1.8* DOWN).scale(0.65)
        self.play(Create(code))
        return code

    def construct(self):

        # Title Text
        title = Text("Merge Sorted Array", gradient=[BLUE, PURPLE]).move_to(3 * UP).scale(1.2)
        self.add(title)

        # Code snippet at the bottom
        merge_sorted_array_code = """
void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int i = m - 1, j = n - 1, k = m + n - 1;
    while (i >= 0 && j >= 0) {
        if (nums2[j] >= nums1[i]) {
            nums1[k] = nums2[j];
            j--;
        } else {
            nums1[k] = nums1[i];
            i--;
        }
        k--;
    }
    while (j >= 0) {
        nums1[k] = nums2[j];
        j--;
        k--;
    }
}
        """
        code_display = self.display_code(merge_sorted_array_code)

        # Array setup
        nums1 = [1, 2, 4, 6, 0, 0, 0, 0, 0]
        nums2 = [3, 5, 7, 8, 9]
        m, n = 4, 5

        nums1_squares = VGroup(*[Square().scale(0.3) for _ in range(len(nums1))]).arrange(RIGHT, buff=0.1).move_to(2*UP)
        nums1_tex = VGroup(*[MathTex(str(num)).scale(0.7) for num in nums1])
        [nums1_tex[i].move_to(nums1_squares[i].get_center()) for i in range(len(nums1))]

        nums2_squares = VGroup(*[Square().scale(0.3) for _ in range(len(nums2))]).arrange(RIGHT, buff=0.1).next_to(nums1_squares, DOWN, buff=0.5)
        nums2_tex = VGroup(*[MathTex(str(num)).scale(0.7) for num in nums2])
        [nums2_tex[i].move_to(nums2_squares[i].get_center()) for i in range(len(nums2))]

        self.play(Create(nums1_squares), Create(nums1_tex), Create(nums2_squares), Create(nums2_tex))

        i, j, k = m - 1, n - 1, m + n - 1
        # Merge Sorted Array Animation
        i_pointer = self.create_pointer(nums1_tex[i].get_center(), "i") if i >= 0 else None
        j_pointer = self.create_pointer(nums2_tex[j].get_center(), "j") if j >= 0 else None
        k_pointer = self.create_pointer(nums1_squares[k].get_center(), "k")

        if i_pointer:
            self.play(Create(i_pointer))
        if j_pointer:
            self.play(Create(j_pointer))
        self.play(Create(k_pointer))

        while k >= 0:
            # Update pointer positions
            if i_pointer:
                self.play(i_pointer.animate.next_to(nums1_tex[i].get_center(), DOWN), run_time=0.5)
            if j_pointer:
                self.play(j_pointer.animate.next_to(nums2_tex[j].get_center(), DOWN), run_time=0.5)
            self.play(k_pointer.animate.next_to(nums1_squares[k].get_center(), DOWN), run_time=0.5)

            if i >= 0 and j >= 0 and nums1[i] > nums2[j]:
                # Move nums1[i] to nums1[k]
                self.play(Transform(nums1_tex[k], MathTex(str(nums1[i])).move_to(nums1_squares[k].get_center())))
                nums1[k] = nums1[i]
                i -= 1
            elif j >= 0:
                # Move nums2[j] to nums1[k]
                self.play(Transform(nums1_tex[k], MathTex(str(nums2[j])).move_to(nums1_squares[k].get_center())))
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        # Final wait before ending the scene
        self.play(FadeOut(code_display))
        self.wait(1)