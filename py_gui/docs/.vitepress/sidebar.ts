import { DefaultTheme } from "vitepress";

export const sidebar: DefaultTheme.Sidebar = {
     
    "/": [
        {
            text: "教程",
            collapsible: true,
            items: [
                { text: "首页", link: "/guide/index" },
                { text: "pyinstaller", link: "/guide/pyinstaller" },
                { text: "nuitka", link: "/guide/nuitka" },
                { text: "pysider", link: "/guide/pysider" },

            ],
        },
    ],
};
