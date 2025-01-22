from manim import *

class Stock(Scene):
    def create_pointer(self, position, label_text):
        """Creates a pointer with a label below the given position."""
        pointer = Triangle(fill_opacity=1, color=RED).scale(0.2)
        pointer.next_to(position, DOWN)
        label = Text(label_text, font_size=24).next_to(pointer, DOWN * 0.2)
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
        ).move_to(1.5 * DOWN + RIGHT).scale(0.8)
        self.play(Create(code))
        return code

    def construct(self):
        # Title Text
        title = Text("Best Time to Buy and Sell Stock", gradient=[BLUE, PURPLE]).move_to(3 * UP).scale(1.2)
        self.add(title)

        # Code snippet at the bottom
        stock_code = """
int maxProfit(vector<int>& prices) {
    int MaxProfit = 0, MinPrice = prices[0];
    for(int i=1;i<prices.size();i++){
        if(MinPrice < prices[i]){
            MaxProfit = max(MaxProfit, prices[i]-MinPrice);
        }
        MinPrice = min(MinPrice, prices[i]);
    }
    return MaxProfit;
}
        """
        code_display = self.display_code(stock_code)

        # Prices setup
        prices = [7, 5, 3, 6, 1, 8, 2, 9, 10, 5]
        array = VGroup(*[Square().scale(0.5) for _ in range(len(prices))]).arrange(RIGHT, buff=0.1).move_to(1.5 * UP)
        price_tex = VGroup(*[MathTex(str(price)) for price in prices]).scale(1.5).arrange(RIGHT).scale(0.8)
        [price_tex[i].move_to(array[i].get_center()) for i in range(len(prices))]
        
        self.play(Create(array), Create(price_tex))
        
        # Initial MaxProfit and MinPrice values
        max_profit_text = Tex("MaxProfit = ", "0")
        min_price_text = Tex("MinPrice =", "7")
        VGroup(max_profit_text, min_price_text).arrange(DOWN, aligned_edge=LEFT, buff=0.5).shift(5 * LEFT + DOWN).scale(0.8)
        self.play(Write(max_profit_text), Write(min_price_text),Create(SurroundingRectangle(VGroup(max_profit_text,min_price_text))))

        # Best Time to Buy and Sell Stock Animation
        max_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            # i Pointer
            i_pointer = self.create_pointer(price_tex[i].get_center(), "i")
            self.play(Create(i_pointer))
            
            # Check for max profit and update if conditions are met
            if prices[i] > min_price:
                profit = prices[i] - min_price
                if profit > max_profit:
                    max_profit = profit
                    new_max_profit_text = Tex(f"{max_profit}").move_to(max_profit_text[1].get_center())
                    self.play(Transform(max_profit_text[1], new_max_profit_text))

            # Update MinPrice if the current price is lower
            if prices[i] < min_price:
                min_price = prices[i]
                new_min_price_text = Tex(f"{min_price}").move_to(min_price_text[1].get_center())
                self.play(Transform(min_price_text[1], new_min_price_text))

            # Highlight the current price being considered
            self.play(price_tex[i].animate.set_color(YELLOW))
            self.wait(0.5)
            self.play(price_tex[i].animate.set_color(WHITE))
            self.play(FadeOut(i_pointer))

        # Final wait before ending the scene
        self.play(FadeOut(code_display), FadeOut(max_profit_text), FadeOut(min_price_text))
        self.wait(1)

class Stock1(Scene):
    def create_pointer(self, position, label_text):
        """Creates a pointer with a label below the given position."""
        pointer = Triangle(fill_opacity=1, color=RED).scale(0.2)
        pointer.next_to(position, DOWN)
        label = Text(label_text, font_size=24).next_to(pointer, DOWN * 0.2)
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
        ).move_to(1.5 * DOWN + RIGHT).scale(0.8)
        self.play(Create(code))
        return code

    def construct(self):
        # Title Text
        title = Text("Best Time to Buy and Sell Stock", gradient=[BLUE, PURPLE]).move_to(3 * UP).scale(1.2)
        self.add(title)

        # Code snippet at the bottom
        stock_code = """
int maxProfit(vector<int>& prices) {
    int MaxProfit = 0, MinPrice = prices[0];
    for(int i=1;i<prices.size();i++){
        if(MinPrice < prices[i]){
            MaxProfit = max(MaxProfit, prices[i]-MinPrice);
        }
        MinPrice = min(MinPrice, prices[i]);
    }
    return MaxProfit;
}
        """
        code_display = self.display_code(stock_code)

        # Prices setup
        prices = [7, 5, 3, 6, 1, 8, 2, 9, 10, 5]
        array = VGroup(*[Square().scale(0.5) for _ in range(len(prices))]).arrange(RIGHT, buff=0.1).move_to(1.5 * UP)
        price_tex = VGroup(*[MathTex(str(price)) for price in prices]).scale(1.5).arrange(RIGHT).scale(0.8)
        [price_tex[i].move_to(array[i].get_center()) for i in range(len(prices))]
        
        self.play(Create(array), Create(price_tex))
        
        # Initial MaxProfit and MinPrice values
        max_profit_text = Tex("MaxProfit = ", "0")
        min_price_text = Tex("MinPrice =", "7")
        VGroup(max_profit_text, min_price_text).arrange(DOWN, aligned_edge=LEFT, buff=0.5).shift(5 * LEFT + DOWN).scale(0.8)
        self.play(Write(max_profit_text), Write(min_price_text), Create(SurroundingRectangle(VGroup(max_profit_text, min_price_text))))

        # Best Time to Buy and Sell Stock Animation
        max_profit = 0
        min_price = prices[0]
        buy_index = 0  # Index where we should buy
        sell_index = 0  # Index where we should sell

        for i in range(1, len(prices)):
            # i Pointer
            i_pointer = self.create_pointer(price_tex[i].get_center(), "i")
            self.play(Create(i_pointer))
            
            # Check for max profit and update if conditions are met
            if prices[i] > min_price:
                profit = prices[i] - min_price
                if profit > max_profit:
                    max_profit = profit
                    sell_index = i  # Update sell index when we find a new max profit
                    new_max_profit_text = Tex(f"{max_profit}").move_to(max_profit_text[1].get_center())
                    self.play(Transform(max_profit_text[1], new_max_profit_text))

            # Update MinPrice if the current price is lower
            if prices[i] < min_price:
                min_price = prices[i]
                buy_index = i  # Update buy index when we find a new min price
                new_min_price_text = Tex(f"{min_price}").move_to(min_price_text[1].get_center())
                self.play(Transform(min_price_text[1], new_min_price_text))

            # Highlight the current price being considered
            self.play(price_tex[i].animate.set_color(YELLOW))
            self.wait(0.5)
            self.play(price_tex[i].animate.set_color(WHITE))
            self.play(FadeOut(i_pointer))

        # Highlight the best buy and sell positions
        buy_pointer = self.create_pointer(price_tex[buy_index].get_center(), f"Buy at Day {buy_index}")
        sell_pointer = self.create_pointer(price_tex[sell_index].get_center(), f"Sell at Day {sell_index}")

        self.play(Create(buy_pointer), Create(sell_pointer))
        self.wait()
        # Final wait before ending the scene
        self.play(FadeOut(*self.mobjects))
        self.wait(1)