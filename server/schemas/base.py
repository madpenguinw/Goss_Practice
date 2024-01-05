from pydantic import BaseModel


class BaseForm(BaseModel):
    class Config:
        populate_by_name = True

        @classmethod
        def alias_generator(cls, snake_str: str) -> str:
            """Return lowerCamelCase."""
            first_char = snake_str[0]
            if first_char == "_":
                return snake_str
            elif first_char.isupper():
                snake_str = first_char.lower() + snake_str[1:]
            first, *others = snake_str.split("_")
            words = [first.lower()]
            words.extend(o.capitalize() for o in others)
            return "".join(words)

        @classmethod
        def snake_case_generator(cls, camel_str: str) -> str:
            """Return snake_case."""
            result = []
            for char in camel_str:
                if char.isupper():
                    result.append("_")
                    result.append(char.lower())
                else:
                    result.append(char)
            return "".join(result)

    def json(self, *args, **kwargs):
        """Override json() method to use snake_case for field names."""
        kwargs["exclude_unset"] = True
        kwargs["by_alias"] = True
        kwargs["skip_defaults"] = True
        return super().json(*args, **kwargs)
