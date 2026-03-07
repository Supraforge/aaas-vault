# Next.js 15 Init

Next.js 15 프로젝트를 ShadCN, Zustand, Tanstack Query, Drizzle ORM과 함께 App Router 패턴으로 자동 세팅

## 주요 기능

- ✅ Next.js 15 (App Router)
- ✅ TypeScript (Strict Mode)
- ✅ Tailwind CSS + ShadCN/ui
- ✅ Zustand (클라이언트 상태 관리)
- ✅ Tanstack Query (서버 상태 관리)
- ✅ React Hook Form + Zod (폼 검증)
- ✅ Drizzle ORM (PostgreSQL 또는 SQLite)
- ✅ Better Auth (인증)
- ✅ Framer Motion (애니메이션)
- ✅ ESLint + Build 검증

## 검증 기준

모든 프로젝트는 다음 두 가지 검증을 **반드시** 통과해야 합니다:

1. **ESLint**: `npm run lint` 또는 `pnpm lint` → 0 errors
2. **Build**: `npm run build` 또는 `pnpm build` → 성공

## Structure

- `SKILL.md` - Main skill instructions
- `references/` - Detailed documentation loaded as needed
  - `setup-guide.md` - 완전한 구현 가이드 (PostgreSQL/SQLite, Next.js 15 params Promise 등)
- `scripts/` - Executable code for deterministic operations
- `assets/` - Templates, images, or other resources

## Usage

This skill is automatically discovered by Claude when relevant to the task.
