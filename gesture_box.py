from kivy.gesture import GestureDatabase
from kivy.uix.boxlayout import BoxLayout
from kivy.gesture import Gesture

gesture_strings = {
    'left_to_right_line': 'eNq1l91u4zYQhe/1IvHNGvPL4byA97ZAHqBIEyExdpsItrftvn3JoRNLRR2qQO2LOD4afuLMIUfUZv9t/8fP7fN4PP04jMPX8/cEw+ZpwuH+7vXh9/FumKj8W754ON7fHU+Ht2/jsfyUYfN90mHzr5D7CBumVFFWxk9v+9dTHZbrML8y7JcaNUzYZlCn8LMMQRp2sAUwMyGXZJAlaarT+ate5mH3BbaihpZTZs6qGXA4/vbw+V0k7qLD8/sNQAE1GXtGdMBcMn5+p+OCDqmPj9zRGv5L5SczRPVsksCy2gXPtpy89PE58H7BIwiYEiuCGyrO8ZIhX8rn1sVTWEA4wwsI52woxuUeNscTJS5/chZA0n5tiILO6+gAGRXEgNCFV8w9jCVdRSdZzr2/biiMJVtVeVwaCytmH8aS3wjPYSzjqmVZ7zdflv3icDjLfCt8WMt6K3xYy/M9y8hinogziUhZgDM+zXcVAvX54S37rfgS5gr2W1qlp9IyUwbSUjdW6fccCXOFb4UPc0VX4dMCL/2FL+Gt2Cq6q0rW7CyYnHRF5cNZ8TV0JJz7vqLZa/iqM18F2ZwRWCSXXvGBVja+tIvcb8Uanir30eaYxZXcMmiiFejwU7WLLn19juY+ObxU65MNwC/Nv98BNHxU///JKTxMq/Ymc6kIEamBMvkKeLiY+Dbw8DGt2pfsxunSkrUPDyuT3QYebqZVu1L0Py5CC0MNbwMPQ62/LbU8JQgZU8L6+Mh9crhpFzcRBSFpZrDSmKQ0+Q82L9qgV3Z9B3g8jOPrx4neUj3SlzPVZoectzDsGKl8nSbLw0MVfSF6iAJzMUMTWyT41ucfqREYEcrvETGMQkyNBbmJ3MRzpDVRmpgXooZo2sTUxBRixoVoIbotxEiPUBfMSI/Y5lPySK+cLueT98iIDK/m7JFe8fd6RORKDtcjpEXY9YioQkuqGIJtclGF8pBaiFEFJlmIUQV+d/4sRhXK8rl61/IIjBDjT0KiQvxJdvVQVELK0f2f1z6mUnZMhNSf808aWnpLrcZLi29VRzlTtKnnguhZLWVqm+Jl3D+/nOrraDmE76rDRfxz/3R6CS0PxWlt6unt+3h4eH0c44rHw7Xq5/3663R4e/rxGKzyJryjrVk549QXFC1NJHnte9u/ASgoChI=',
    'right_to_left_line': 'eNq1l0tu2zAQhve8SLyJQc6L5AXcbYEcoHATITHS2oLttM3tSw4ViUofzIaahezfMx85+mlK2hyeDz9et4/D5fpyHsyn6Txas3kYnbm7Oe6/DzdmhPQxndBc7m4u1/Ppebikr2Q230Y2m79C7jTNjJJRPtWPp8PxmstCLov/KPucs8zoygzyFF5TiQOzs1uLFKrwkfN8fuXfMf9OiMRxiTTdr/v/D0M6DJvHtxHWEby5PBY4erAVm9ps7dz5mQ2r6TPjwgYRcnO00UHRsQMa9MKDm9EuRJyDkgUzGoJzQZZos0HZuLChDljIwuCro01WH2Hy8TahLfpQB/FCdyu6hDZerQTfC692QlzwzkoVbMNMd2RXlwaadFRH0XWiq6eIH6FbH6KrFmN7NaL6ityJrrai/xCdsaa3txZUU7Eydc2OIU5wHTgEh3MQtRcNqa3kuvHVWKqMtY6rIIlUDRAiiF+i/ZcltZa4G1/NpWX7TQ7WW7vwQndCNT20lw6puxT70Fm9ZdeJrs7ysg2/u+tVcCCxgeeQ9rJntZW5D1w95Y/sw7f51seC1apv49VUjp3woq6K64VXW6XeiWFFB1zohBIjzZH8auLVWOFeeLVWfC+8WiuVtUCrCGHBs3MrfJPu1VnvOtHVWI+d6Oqrr3xFXt1IquvOIkx2Dl2T+Y3g/jwMx/n53kt+wE9b9GaX0rfW7CDEbawPMtfRB7NPGeBLRkinJEYV7SSyisFmkcMkYhFdEW0RbRFBRQ4q+ikTVaRJdEUkFYGLOJVzFimmzPqQKkM0Y5rKm+hV5IkFRdT2kj1FpCJqe+lJoohexajt4Vu5FFHbQ7B1J1HbKy3sQGIRtT3A0p7gn1c6aq/gylR4Kku9FvuehsPj0zUZF1OjaN/V6zvfz8PD9SlneLMjynNK4vX0bTjvj/f5BTEGfXzM8rTMvozn08PLvXJj4m6tOC/p/QERIW1oebff/gayUMeJ',
    'bottom_to_top_line': 'eNq1l9tOJEcMhu/7ReAmyMey/QLsbSQeICIwArQbGDGzSfbt43IN3Q1id1DQ9AXDuO3PVf5dhzl/+Prw94+Lu81u//15M305fG5hOr/d4nR19nj91+Zs2lL+mx887a7Odvvnp6+bXX6V6fzbVqfzdyFX5TZtW0dZxm+fHh73Pcx7WPwk7PfuNW1xjKAP4UeGIE2Xv8GFBBMaqFBjbRp9OP/211yvAUDZmQKoGSCKyrT78/rXiaQS6XT3kkPaksEDp91dxycdiR21WUNByk87Dq/Joy1wAm/amMFyLkqy0AmQWUE1vBFmouN0L3rMdA4FUuewrJNn8gWuDChNSCWUjqOpyk+4oMUVhRDdG4P4gs5vLYQoEMlZoB2HU8F5gaMEkTi0LIIqyKfoJSgtglLGKzTRCHHOcn0GXoLSIihxhBs4IKR6kVIvNTd3FeEUJMuG9oGql6AUp6FzacqLptmLL52ibNLo//cLl6S8SIocc7MEhHyq0bkkZT0RvTTlRVNozVu2hiK2LHPYp+ilKcdp6FKaykHTvkdBbVpi5M1ziS2bl0RTPfQ7BPhxdmkqfBJ2KSp6EnbpKTazHZbdXExXzQLZ/6bu5BqpiRzfAKTklDgJXEtNndVEBQy2cMkiIGW5FjiBZFIYy5Q/UBYtOZVPAy89ddYzT8pamdrAKM+5A7vOaJ/PZ4yUm4/DS1C108BLUI2TwFsJ2mZBKWw55dhdVnTMHqEsfGTq4Fx8R+ElaOPTwEvQNgvKCSQhDwFtnrvXCk7ZRZKXg8hzyjPBcXgJ2mZBs+TYLPRwNfI12yO3wnzNTQlIPlDzErTNgubyXLGtreAsyAANKHKNQhxnW+lpeBJ2yWmznJKxhoyWXSdqazW5GQrwS2WOL08rNW1WM/skhDHvnyrmyVvD4yCkRB5BeS3q9H7tv3nebB7nS3xONm/xeQc+vxSQC5guLS7i1TPtt+bT9a8dYjhEdwjPv/utQ9mQug3B+71+ebh74PDg10BJdzwwaHi0YnAbRl4bxV9HW/eQtYfaO6l1eOjrVy3dzd4Btp+ONGAMylazzV8376T0tYfoCJsL9xZMNjxilLHXb7pkoLcDTo9RRtDyoBhho3KAZWw8jFU5jsHyUc6QYazwHvBmJOmhw4PL4yBNtGGsBHKQJmwYoYxyGEpNnL2aQ7oa3RhrY8MyIsCw+rDawZoTHN17v3m4u9/3n4pAfQbdIc3/PNzu78ua3U8+jPunb5vn68ebTb2QOiy7/bC2/tg+P91+vxkwzbALy6eZWvP88Yna1/rFf76K9Qc='
}

gestures = GestureDatabase()
for name, gesture_stringo in gesture_strings.items():
    gesture = gestures.str_to_gesture(gesture_stringo)
    gesture.name = name
    gestures.add_gesture(gesture)

class GestureBox(BoxLayout):

    def __init__(self,**kwargs):
        for name in gesture_strings:
            self.register_event_type("on_{}".format(name))
        super(GestureBox, self).__init__(**kwargs)

    def on_left_to_right_line(self):
        pass

    def on_right_to_left_line(self):
        pass

    def on_bottom_to_top_line(self):
        pass

    def on_touch_down(self, touch):
        touch.ud['gesture_path'] = [(touch.x, touch.y)]
        super(GestureBox, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        touch.ud['gesture_path'].append((touch.x, touch.y))
        super(GestureBox, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        if 'gesture_path' in touch.ud:
            gesture = Gesture()
            gesture.add_stroke(touch.ud['gesture_path'])
            gesture.normalize()
            match = gestures.find(gesture, minscore= 0.90)
            if match:
                print('{} happended'.format(match[1].name))
                self.dispatch('on_{}'.format(match[1].name))
        super(GestureBox, self).on_touch_up(touch)
