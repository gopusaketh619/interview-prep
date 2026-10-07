-- =============================================================================
-- 40. Bill of materials cost roll-up                           Difficulty: Hard
-- Topic: Recursive CTEs (graph explosion)     Inspired by: manufacturing / supply-chain BOM questions (Amazon, Tesla)
-- Tables: parts, bom                          Schema: python3 run.py --schema misc
-- =============================================================================
-- bom(parent_id, child_id, qty) says one parent is built from `qty` units of the child. Only base
-- parts have a unit_cost; assemblies cost the sum of their components. Return the total cost of
-- every top-level product.
--
-- Clarifications:
--   * A top-level product is a part that is a parent in bom but never a child.
--   * Assemblies can be nested (a Wheel is used inside a Bike); quantities multiply down the tree.
--
-- Output columns: product, total_cost
-- Row order: any
-- Check: python3 run.py 40
-- =============================================================================

-- YOUR SQL BELOW

