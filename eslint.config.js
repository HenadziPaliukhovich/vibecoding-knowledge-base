import html from "eslint-plugin-html";

export default [
  {
    files: ["**/*.html"],
    plugins: { html },
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: "script",
      globals: {
        window: "readonly",
        document: "readonly",
        localStorage: "readonly",
        navigator: "readonly",
        console: "readonly",
      },
    },
    rules: {
      "no-undef": "error",
      "no-unused-vars": "warn",
      "no-redeclare": "error",
      "no-var": "error",
      eqeqeq: "error",
    },
  },
  {
    files: ["**/*.js"],
    languageOptions: { ecmaVersion: 2022, sourceType: "script" },
    rules: {
      "no-undef": "error",
      "no-unused-vars": "warn",
      "no-redeclare": "error",
      "no-var": "error",
      eqeqeq: "error",
    },
  },
];
