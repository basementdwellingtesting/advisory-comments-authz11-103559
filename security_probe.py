"""Inert fixture used only to test Copilot code review activation."""


def may_delete_repository(user_role: str) -> bool:
    # Intentional bug for the review control: ordinary members must not pass.
    return user_role in {"admin", "member"}
