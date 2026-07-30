def style_chart(fig):

    # ---------- Style all lines ----------
    fig.update_traces(
        line=dict(width=2.8),
        hovertemplate=None
    )

    # ---------- Layout ----------
    fig.update_layout(

        template=None,

        paper_bgcolor="#0B0F19",
        plot_bgcolor="#111827",

        font=dict(
            family="Inter",
            size=14,
            color="#F3F4F6"
        ),

        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),

        hovermode="x unified",

        legend=dict(
            orientation="h",
            y=1.05,
            x=0,
            bgcolor="rgba(0,0,0,0)",
            font=dict(size=13)
        ),

        hoverlabel=dict(
            bgcolor="#1F2937",
            font_size=13,
            font_family="Inter"
        )
    )

    # ---------- X Axis ----------
    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        showline=False,
        tickfont=dict(color="#9CA3AF")
    )

    # ---------- Y Axis ----------
    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(255,255,255,0.07)",
        gridwidth=1,
        zeroline=False,
        showline=False,
        tickfont=dict(color="#9CA3AF")
    )

    return fig