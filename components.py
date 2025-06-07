import streamlit as st


def difficulty_slider():
    difficulty = st.slider(
        "Course Difficulty",
        min_value=0,
        max_value=100,
        value=50,
        step=1,
    )

    st.markdown(
        """
        <div style='display: flex; justify-content: space-between; padding: 0px 5px; font-size: 0.9em; color: #888;'>
            <span>🏆 Beginner</span>
            <span>⚖️ Intermediate</span>
            <span>🔥 Pro-level</span>
        </div>
        <br>
        """,
        unsafe_allow_html=True
    )

    # Map difficulty to course characteristics
    a = 0.045 - difficulty * 0.016 / 100
    b = 4.5 + difficulty * 0.53 / 100
    c = 140 + difficulty

    return a, b, c


def player_input():
    # Slider for number of players
    num_players = st.slider("Number of players", min_value=1, max_value=12, value=2)

    # Flexbox CSS for paired inputs
    st.markdown(
        """
        <style>
        .player-row {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 10px;
        }
        .player-col {
            flex: 1 1 45%;
            min-width: 120px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Render player input pairs
    player_names = []
    player_ratings = []

    for i in range(1, num_players + 1):
        st.markdown('<div class="player-row">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            name = st.text_input(
                f"Player {i}",
                key=f"player_name_{i}",
                placeholder=f"Player {i}",
                label_visibility="collapsed",
            )
            player_names.append(name)
        
        with col2:
            rating = st.number_input(
                f"Rating",
                key=f"player_rating_{i}",
                min_value=50,
                max_value=350,
                value=200,
                step=1,
                label_visibility="collapsed",
            )
            player_ratings.append(rating)
        
        st.markdown('</div>', unsafe_allow_html=True)

    return player_names, player_ratings


def hero_box_ratings():
    st.markdown(
        """
        <div style="
            background-color:#A8D5BA;
            padding:15px 20px;
            border-radius:12px;
            margin-bottom:20px;
            border: 1px solid #DDD;
        ">
        <h4 style="color:#000; margin-top: 0;">How UDisc Round Rating is Calculated</h4>
        <p style="color:#000; font-size: 1em; line-height: 1.5;">
        UDisc ratings are calculated based on 3 course-specific constants which are used to define as curve on which ratings are located.

        - **c<sub>1</sub>**: Controls the curvature of the curve.
        - **c<sub>2</sub>**: Controls the slope of the curve. This is higher for easier course to create better score separation.
        - **b**: Controls the baseline rating. The baseline rating determines the rating expected to play the course in even par.

        The rating <em>R</em> for a round with a score of <em>s</em>, relative to par (e.g. <em>s=-2</em> for a round in 2 under par), is calculated via the quadratic equation:
        </p></div>
        """,
        unsafe_allow_html=True
    )

    # Equation — rendered properly
    st.markdown(r"""
    $$
    c_1s^2 - c_2s + b = R
    $$
    """
    )

    st.write("")
    st.markdown('*c<sub>1</sub>, c<sub>2</sub>, and b are set as "sensible defaults" and can be adjusted through the slighter, changed manually or left untouched.*',
    unsafe_allow_html=True,
    )


def advanced_settings():
    st.markdown("### Adjust Course Characteristics")
    st.markdown("Use the slider - or set the course characteristics manually below - to adjust the calculations to the proper course difficulty.")

    st.write("")
    st.markdown("#### Select Course Difficulty")
    c_1_default, c_2_default, b_default = difficulty_slider()

    hero_box_ratings()

    st.write("")
    st.markdown("#### Set Course Characteristics")

    c1, c2, c3 = st.columns(3)
    with c1:
        c_1 = st.number_input(
            "Course characteristic c1",
            min_value=0.01,
            max_value=0.05,
            value=c_1_default,
            step=0.001,
            format="%.4f",
        )
    with c2:
        c_2 = st.number_input(
        "Course characteristic c2",
            min_value=3.0,
            max_value=7.0,
            value=c_2_default,
            step=0.01,
        )
    with c3:
        b_ = st.number_input(
        "Course characteristic b",
            min_value=50.0,
            max_value=350.0,
            value=float(b_default),
            step=1.0,
        )
    return c_1, c_2, b_