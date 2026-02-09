"""Streamlit entrypoint for DecisionPilot AI."""

codex/build-decisionpilot-ai-enterprise-platform-k26tfx
from app import main as app_main


def run():
    """Run the DecisionPilot AI Streamlit application."""
    app_main()


if __name__ == "__main__":
    run()
=======
    def create_kpi_trends(self, kpi_df: pd.DataFrame) -> go.Figure:
        """Create KPI trend dashboard"""
        df = kpi_df.copy()
        df['date'] = pd.to_datetime(df['date'])

        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=(
                'Net Promoter Score (NPS)',
                'Churn Rate',
                'Pipeline Value',
                'Employee Engagement'
            )
        )

        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['nps'],
            mode='lines+markers',
            line=dict(color=self.color_scheme['primary'], width=3),
            name='NPS'
        ), row=1, col=1)

        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['churn_rate'] * 100,
            mode='lines+markers',
            line=dict(color=self.color_scheme['danger'], width=3),
            name='Churn %'
        ), row=1, col=2)

        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['pipeline_value'],
            mode='lines+markers',
            line=dict(color=self.color_scheme['success'], width=3),
            name='Pipeline'
        ), row=2, col=1)

        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['employee_engagement'],
            mode='lines+markers',
            line=dict(color=self.color_scheme['warning'], width=3),
            name='Engagement'
        ), row=2, col=2)

        fig.update_layout(height=600, showlegend=False, template='plotly_white')

        return fig


if __name__ == "__main__":
    from app import main

    main()
main